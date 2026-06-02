import time

import pytest

from leetcode.concurrency.asyncio import web_crawler

_USER_PROFILES: dict[int, web_crawler.UserProfile] = {
    1: web_crawler.UserProfile(1, "facebook", "John Doe"),
    2: web_crawler.UserProfile(2, "twitter", "Jane Doe"),
    3: web_crawler.UserProfile(3, "linkedin", "Bob Smith"),
}


async def test_fetch_user_profiles():
    """Happy path test for fetching user profiles."""
    user_ids = [1, 2, 3]
    user_fetcher = web_crawler.UserProfileFetcher(_USER_PROFILES, 0, 0, 0, 100)
    user_data = await web_crawler.fetch_user_profiles(user_ids, user_fetcher)

    assert set(user_data) == set(_USER_PROFILES.values())


async def test_fetch_user_profiles_failure():
    """Test that all requests fail and max retries are reached."""
    user_ids = [1, 2]
    # failure_rate = 1.0 means it will always fail with FetchError
    user_fetcher = web_crawler.UserProfileFetcher(
        _USER_PROFILES, failure_rate=1.0, max_retries=2
    )
    user_data = await web_crawler.fetch_user_profiles(user_ids, user_fetcher)

    assert len(user_data) == 0
    # 2 IDs, max_retries=2. First attempt fails, 1 retry happens.
    # Total retries should be 2 (one for each user_id)
    assert user_fetcher.total_num_retries == 2


@pytest.mark.timeout(2)
async def test_fetch_user_profiles_timeout():
    """Test that requests timeout and max retries are reached."""
    user_ids = [1]
    # min_delay > TIMEOUT_SECONDS (2s)
    user_fetcher = web_crawler.UserProfileFetcher(
        _USER_PROFILES, min_delay=2.1, max_delay=2.1, max_retries=2
    )
    user_data = await web_crawler.fetch_user_profiles(user_ids, user_fetcher)

    assert len(user_data) == 0
    assert user_fetcher.total_num_retries == 1


async def test_fetch_user_profiles_non_existent():
    """Test fetching user IDs that don't exist in the data."""
    user_ids = [99, 100]
    user_fetcher = web_crawler.UserProfileFetcher(_USER_PROFILES)
    user_data = await web_crawler.fetch_user_profiles(user_ids, user_fetcher)

    assert len(user_data) == 0


async def test_rate_limiting():
    """Test that rate_limit_per_second is respected."""
    user_ids = [1, 2, 3]
    # 2 requests per second. aiolimiter (v2+) with max_rate=2, time_period=1:
    # 1st request at T=0
    # 2nd request at T=0
    # 3rd request at T=0.5
    # Total time should be at least 0.5 seconds.
    user_fetcher = web_crawler.UserProfileFetcher(
        _USER_PROFILES, rate_limit_per_second=2
    )

    start_time = time.perf_counter()
    user_data = await web_crawler.fetch_user_profiles(user_ids, user_fetcher)
    duration = time.perf_counter() - start_time

    assert len(user_data) == 3
    assert duration >= 0.5


@pytest.mark.timeout(2)
async def test_global_concurrency_limiting():
    """Test that MAX_CONCURRENT_REQUESTS is respected."""
    user_ids = [1, 2, 3, 4, 5, 6]
    user_profiles = {
        1: web_crawler.UserProfile(1, "facebook", "John Doe"),
        2: web_crawler.UserProfile(2, "twitter", "Jane Doe"),
        3: web_crawler.UserProfile(3, "linkedin", "Bob Smith"),
        4: web_crawler.UserProfile(4, "github", "Alice Johnson"),
        5: web_crawler.UserProfile(5, "instagram", "Emily Davis"),
        6: web_crawler.UserProfile(6, "reddit", "Michael Brown"),
    }

    # We want to check that only 5 requests happen at a time (MAX_CONCURRENT_REQUESTS=5)
    # 1-5 will start at T=0. 6 will start only after one of 1-5 finishes.
    # We use a small delay (0.5s) to stay well within TIMEOUT_SECONDS (2s).
    # 1-5 finish at T=0.5. 6 finishes at T=1.0.
    # Total time should be at least 1.0 second.
    user_fetcher = web_crawler.UserProfileFetcher(
        user_profiles, min_delay=0.5, max_delay=0.5
    )

    start_time = time.perf_counter()
    user_data = await web_crawler.fetch_user_profiles(user_ids, user_fetcher)
    duration = time.perf_counter() - start_time

    assert len(user_data) == 6
    assert duration >= 1.0
