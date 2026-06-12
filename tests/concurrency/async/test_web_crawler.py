import time

import pytest

from leetcode.concurrency.asyncio import web_crawler

_USER_PROFILES: dict[int, web_crawler.UserProfile] = {
    1: web_crawler.UserProfile(1, "facebook", "John Doe", 1),
    2: web_crawler.UserProfile(2, "twitter", "Jane Doe", 1),
    3: web_crawler.UserProfile(3, "linkedin", "Bob Smith", 1),
}

_USERS = [
    web_crawler.UserProfileRequestData(uid, p.source, p.priority)
    for uid, p in _USER_PROFILES.items()
]


async def test_fetch_user_profiles():
    """Happy path test for fetching user profiles."""
    user_fetcher = web_crawler.UserProfileFetcher(_USER_PROFILES, 0, 0, 0, 100)
    user_data = await web_crawler.fetch_user_profiles(_USERS, user_fetcher)

    assert set(user_data) == set(_USER_PROFILES.values())


async def test_fetch_user_profiles_failure():
    """Test that all requests fail and max retries are reached."""
    users = [
        web_crawler.UserProfileRequestData(1, "facebook", 1),
        web_crawler.UserProfileRequestData(2, "twitter", 1),
    ]
    # failure_rate = 1.0 means it will always fail with FetchError
    user_fetcher = web_crawler.UserProfileFetcher(
        _USER_PROFILES, failure_rate=1.0, max_retries=2
    )
    user_data = await web_crawler.fetch_user_profiles(users, user_fetcher)

    assert len(user_data) == 0
    # 2 IDs, max_retries=2. First attempt fails, 1 retry happens.
    # Total retries should be 2 (one for each user_id)
    assert user_fetcher.total_num_retries == 2


@pytest.mark.timeout(2)
@pytest.mark.skip
async def test_fetch_user_profiles_timeout():
    """Test that requests timeout and max retries are reached."""
    users = [web_crawler.UserProfileRequestData(1, "facebook", 1)]
    # min_delay > TIMEOUT_SECONDS (2s)
    user_fetcher = web_crawler.UserProfileFetcher(
        _USER_PROFILES, min_delay=2.1, max_delay=2.1, max_retries=2
    )
    user_data = await web_crawler.fetch_user_profiles(users, user_fetcher)

    assert len(user_data) == 0
    assert user_fetcher.total_num_retries == 1


async def test_fetch_user_profiles_non_existent():
    """Test fetching user IDs that don't exist in the data."""
    users = [
        web_crawler.UserProfileRequestData(99, "facebook", 1),
        web_crawler.UserProfileRequestData(100, "twitter", 1),
    ]
    user_fetcher = web_crawler.UserProfileFetcher(_USER_PROFILES)
    user_data = await web_crawler.fetch_user_profiles(users, user_fetcher)

    assert len(user_data) == 0


async def test_rate_limiting():
    """Test that rate_limit_per_second is respected."""
    # 2 requests per second. aiolimiter (v2+) with max_rate=2, time_period=1:
    # 1st request at T=0
    # 2nd request at T=0
    # 3rd request at T=0.5
    # Total time should be at least 0.5 seconds.
    user_fetcher = web_crawler.UserProfileFetcher(
        _USER_PROFILES, rate_limit_per_second=2
    )

    start_time = time.perf_counter()
    user_data = await web_crawler.fetch_user_profiles(_USERS, user_fetcher)
    duration = time.perf_counter() - start_time

    assert len(user_data) == 3
    assert duration >= 0.5


async def test_circuit_opens_when_failure_rate_exceeded():
    """Circuit opens for a source once its failure rate crosses the threshold."""
    profiles = {1: web_crawler.UserProfile(1, "facebook", "John Doe", 1)}
    user_fetcher = web_crawler.UserProfileFetcher(
        profiles,
        failure_rate=1.0,
        max_retries=1,
        max_source_failure_rate=0.3,
    )

    result = await user_fetcher.fetch_profile(1, "facebook")

    assert result is None
    assert (
        user_fetcher._source_circuit_states["facebook"].status
        == web_crawler.CircuitStatus.OPEN
    )


async def test_open_circuit_skips_requests_during_cooldown():
    """While the circuit is open, requests are skipped without making an API call."""
    profiles = {1: web_crawler.UserProfile(1, "facebook", "John Doe", 1)}
    user_fetcher = web_crawler.UserProfileFetcher(
        profiles,
        failure_rate=1.0,
        max_retries=1,
        max_source_failure_rate=0.3,
    )

    await user_fetcher.fetch_profile(1, "facebook")
    failures_after_trip = user_fetcher.source_metrics["facebook"].num_failures

    result = await user_fetcher.fetch_profile(1, "facebook")

    assert result is None
    # num_failures must not grow — the request was skipped, not attempted
    assert user_fetcher.source_metrics["facebook"].num_failures == failures_after_trip


async def test_failed_probe_keeps_circuit_open():
    """A probe that fails resets the cooldown and keeps the circuit open."""
    profiles = {1: web_crawler.UserProfile(1, "facebook", "John Doe", 1)}
    user_fetcher = web_crawler.UserProfileFetcher(
        profiles,
        failure_rate=1.0,
        max_retries=1,
        max_source_failure_rate=0.3,
    )

    await user_fetcher.fetch_profile(1, "facebook")
    # Simulate the cooldown having elapsed
    user_fetcher._source_circuit_states["facebook"].opened_at = (
        time.monotonic() - web_crawler.SOURCE_RECOVERY_SECONDS - 1
    )

    result = await user_fetcher.fetch_profile(1, "facebook")

    assert result is None
    assert (
        user_fetcher._source_circuit_states["facebook"].status
        == web_crawler.CircuitStatus.OPEN
    )


async def test_successful_probe_closes_circuit():
    """A probe that succeeds transitions the circuit back to closed."""
    profiles = {1: web_crawler.UserProfile(1, "facebook", "John Doe", 1)}
    user_fetcher = web_crawler.UserProfileFetcher(
        profiles,
        failure_rate=1.0,
        max_retries=1,
        max_source_failure_rate=0.3,
    )

    await user_fetcher.fetch_profile(1, "facebook")
    # Simulate cooldown elapsed and source recovered
    user_fetcher._source_circuit_states["facebook"].opened_at = (
        time.monotonic() - web_crawler.SOURCE_RECOVERY_SECONDS - 1
    )
    user_fetcher._failure_rate = 0.0

    result = await user_fetcher.fetch_profile(1, "facebook")

    assert result is not None
    assert result.user_id == 1
    assert (
        user_fetcher._source_circuit_states["facebook"].status
        == web_crawler.CircuitStatus.CLOSED
    )


async def test_circuit_does_not_affect_other_sources():
    """Opening the circuit for one source leaves other sources unaffected."""
    profiles = {
        1: web_crawler.UserProfile(1, "facebook", "John Doe", 1),
        2: web_crawler.UserProfile(2, "twitter", "Jane Doe", 1),
    }
    user_fetcher = web_crawler.UserProfileFetcher(
        profiles,
        failure_rate=1.0,
        max_retries=1,
        max_source_failure_rate=0.3,
    )

    await user_fetcher.fetch_profile(1, "facebook")
    assert (
        user_fetcher._source_circuit_states["facebook"].status
        == web_crawler.CircuitStatus.OPEN
    )

    # Fix the failure rate and fetch from a different source — it should succeed
    user_fetcher._failure_rate = 0.0
    result = await user_fetcher.fetch_profile(2, "twitter")

    assert result is not None
    assert result.user_id == 2


@pytest.mark.timeout(2)
async def test_global_concurrency_limiting():
    """Test that MAX_CONCURRENT_REQUESTS is respected."""
    user_profiles = {
        1: web_crawler.UserProfile(1, "facebook", "John Doe", 1),
        2: web_crawler.UserProfile(2, "twitter", "Jane Doe", 1),
        3: web_crawler.UserProfile(3, "linkedin", "Bob Smith", 1),
        4: web_crawler.UserProfile(4, "github", "Alice Johnson", 1),
        5: web_crawler.UserProfile(5, "instagram", "Emily Davis", 1),
        6: web_crawler.UserProfile(6, "reddit", "Michael Brown", 1),
    }
    users = [
        web_crawler.UserProfileRequestData(uid, p.source, p.priority)
        for uid, p in user_profiles.items()
    ]

    # We want to check that only 5 requests happen at a time (MAX_CONCURRENT_REQUESTS=5)
    # 1-5 will start at T=0. 6 will start only after one of 1-5 finishes.
    # We use a small delay (0.5s) to stay well within TIMEOUT_SECONDS (2s).
    # 1-5 finish at T=0.5. 6 finishes at T=1.0.
    # Total time should be at least 1.0 second.
    user_fetcher = web_crawler.UserProfileFetcher(
        user_profiles, min_delay=0.5, max_delay=0.5
    )

    start_time = time.perf_counter()
    user_data = await web_crawler.fetch_user_profiles(users, user_fetcher)
    duration = time.perf_counter() - start_time

    assert len(user_data) == 6
    assert duration >= 1.0
