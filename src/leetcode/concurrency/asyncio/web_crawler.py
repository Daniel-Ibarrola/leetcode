"""
TODOs:

Concurrency patterns
- Circuit breaker — track failure rate per source (facebook, twitter, etc.) and stop sending requests to a
source that exceeds a threshold, then probe it periodically to see if it recovers
- Priority queue — fetch VIP user IDs before regular ones using asyncio.PriorityQueue
- Batching — group requests into batches of N and process each batch before starting the next, useful for simulating paginated APIs

Resilience
- Per-source rate limits — instead of one global aiolimiter,
  give each source (facebook, github, etc.) its own limiter with different rates
- Jitter on backoff — add randomness to the exponential backoff to
  avoid thundering herd when many retries fire at the same moment
- Deadline propagation — accept a wall-clock deadline at the fetch_user_profiles
  level and cancel remaining requests once it expires

Observability
- Metrics collection — track per-source success rate, p50/p95 latency,
  and retry count; return a stats summary alongside the profiles
- Structured logging — replace print/logging calls with a context dict that
  carries user_id, attempt, and source through every log line

Design / architecture
- Cache layer — add an in-memory TTL cache so repeated lookups for the same user_id skip the API call
- Pluggable fetcher interface — define an abstract BaseProfileFetcher protocol and swap in different backends
(the current simulated one, a real HTTP one) without changing fetch_user_profiles
- Streaming results — replace returning a list with an AsyncGenerator[UserProfile, None] so callers can
process profiles as they arrive instead of waiting for all of
"""

import asyncio
import dataclasses
import time
from typing import Optional
import random
import logging
from statistics import quantiles

import aiolimiter


@dataclasses.dataclass(frozen=True)
class UserProfile:
    user_id: int
    source: str
    name: str


@dataclasses.dataclass
class SourceMetrics:
    num_requests: int
    num_retries: int
    request_times: list[float]

    @property
    def success_rate(self) -> float:
        return self.num_requests / (self.num_requests + self.num_retries)

    @property
    def p50_latency(self) -> float:
        if not self.request_times:
            return 0.0
        return quantiles(self.request_times, n=100)[49]

    @property
    def p95_latency(self) -> float:
        if not self.request_times:
            return 0.0
        return quantiles(self.request_times, n=100)[94]


_USER_PROFILES: dict[int, UserProfile] = {
    1: UserProfile(1, "facebook", "John Doe"),
    2: UserProfile(2, "twitter", "Jane Doe"),
    3: UserProfile(3, "linkedin", "Bob Smith"),
    4: UserProfile(4, "github", "Alice Johnson"),
    5: UserProfile(5, "instagram", "Emily Davis"),
    6: UserProfile(6, "reddit", "Michael Brown"),
    7: UserProfile(7, "tiktok", "Sophia Wilson"),
    8: UserProfile(8, "youtube", "David Lee"),
    9: UserProfile(9, "facebook", "Chris Evans"),
    10: UserProfile(10, "twitter", "Natalie Portman"),
    11: UserProfile(11, "github", "Linus Torvalds"),
    12: UserProfile(12, "linkedin", "Satya Nadella"),
    13: UserProfile(13, "instagram", "Selena Gomez"),
    14: UserProfile(14, "reddit", "Aaron Swartz"),
    15: UserProfile(15, "facebook", "Mark Zuckerberg"),
    16: UserProfile(16, "tiktok", "Charli D'Amelio"),
    17: UserProfile(17, "youtube", "MrBeast"),
    18: UserProfile(18, "twitter", "Elon Musk"),
    19: UserProfile(19, "github", "Guido van Rossum"),
    20: UserProfile(20, "instagram", "Cristiano Ronaldo"),
    21: UserProfile(21, "linkedin", "Jeff Weiner"),
    22: UserProfile(22, "reddit", "Steve Huffman"),
    23: UserProfile(23, "facebook", "Sheryl Sandberg"),
    24: UserProfile(24, "youtube", "Marques Brownlee"),
    25: UserProfile(25, "tiktok", "Khaby Lame"),
}


class FetchError(Exception):
    pass


TIMEOUT_SECONDS = 2
MAX_CONCURRENT_REQUESTS = 5


class UserProfileFetcher:
    def __init__(
        self,
        user_data: Optional[dict[int, UserProfile]] = None,
        failure_rate: float = 0.0,
        min_delay: float = 0.0,
        max_delay: float = 0.0,
        rate_limit_per_second: int = 0,
        max_retries: int = 3,
    ):
        self._user_profiles: dict[int, UserProfile] = user_data or {}
        self._failure_rate = failure_rate
        self._min_delay = min_delay
        self._max_delay = max_delay
        self._max_retries = max_retries
        self._total_num_retries = 0
        self._request_times: list[float] = []
        self._rate_limiter = (
            aiolimiter.AsyncLimiter(rate_limit_per_second, time_period=1)
            if rate_limit_per_second > 0
            else None
        )
        self._source_metrics: dict[str, SourceMetrics] = {}

    @property
    def total_num_retries(self) -> int:
        return self._total_num_retries

    @property
    def average_request_time(self) -> float:
        if not self._request_times:
            return 0.0
        return sum(self._request_times) / len(self._request_times)

    @property
    def source_metrics(self) -> dict[str, SourceMetrics]:
        return self._source_metrics

    async def _call_user_api(self, user_id: int) -> Optional[UserProfile]:
        """
        Fetches the user profile for a given user ID, simulating an asynchronous API call
        with random delay and potential failure.

        :param user_id: The ID of the user whose profile is being fetched.
        :type user_id: int
        :return: The user profile if successfully fetched, or None if the user ID does not
            exist in the profile data.
        :rtype: Optional[UserProfile]
        :raises FetchError: If the API call fails due to simulated failure conditions.
        """
        if self._rate_limiter:
            async with self._rate_limiter:
                return await self._do_call_user_api(user_id)
        return await self._do_call_user_api(user_id)

    async def _do_call_user_api(self, user_id: int) -> Optional[UserProfile]:
        logging.info("Fetching user profile for user_id %s", user_id)

        start_time = time.perf_counter()

        sleep_time = random.uniform(self._min_delay, self._max_delay)
        logging.info("Delay %s seconds", sleep_time)

        await asyncio.sleep(sleep_time)

        if random.random() < self._failure_rate:
            logging.error("Failed to fetch user profile for user_id %s", user_id)
            raise FetchError(f"Failed to fetch user profile for user_id {user_id}")

        end_time = time.perf_counter()
        request_time = end_time - start_time
        self._request_times.append(request_time)

        profile = self._user_profiles.get(user_id)
        if not profile:
            logging.error("User profile not found for user_id %s", user_id)
            raise FetchError(f"User profile not found for user_id {user_id}")

        source_metrics = self._source_metrics.get(profile.source)
        if not source_metrics:
            self._source_metrics[profile.source] = SourceMetrics(
                num_requests=1, num_retries=0, request_times=[request_time]
            )
        else:
            source_metrics.num_requests += 1
            source_metrics.request_times.append(request_time)

        return profile

    async def fetch_profile(self, user_id: int) -> Optional[UserProfile]:
        """
        Fetch the profile of a user asynchronously by making a call to an external API. Retries
        the request several times upon failure due to either `FetchError` or `TimeoutError`. An
        exponential backoff strategy is used for successive retries.

        :param user_id: The unique identifier of the user whose profile needs to be fetched.
        :type user_id: int
        :return: The user's profile if the fetch operation is successful, otherwise None.
        :rtype: Optional[UserProfile]
        """
        sleep_time_on_failure = 0.1
        for attempt in range(self._max_retries):
            try:
                profile = await asyncio.wait_for(
                    self._call_user_api(user_id), timeout=TIMEOUT_SECONDS
                )
                if profile:
                    self._source_metrics[profile.source].num_retries += max(
                        0, attempt - 1
                    )
                return profile
            except (FetchError, TimeoutError) as exc:
                fail_reason = (
                    "FetchError" if isinstance(exc, FetchError) else "TimeoutError"
                )

                if attempt < self._max_retries - 1:
                    self._total_num_retries += 1
                    logging.error(
                        "Fetch failed for user_id %s (%s). Retrying...",
                        user_id,
                        fail_reason,
                    )
                    await asyncio.sleep(sleep_time_on_failure)
                    sleep_time_on_failure *= 2
                else:
                    logging.error(
                        "Max retries reached for user_id %s (%s). Skipping...",
                        user_id,
                        fail_reason,
                    )
                    return None
        return None


async def fetch_user_profiles(
    user_ids: list[int], user_fetcher: UserProfileFetcher
) -> list[UserProfile]:
    """
    Fetch user profiles concurrently with rate limiting.

    This asynchronous function takes a list of user IDs and a UserProfileFetcher
    instance, fetches user profiles concurrently, and enforces a global rate
    limiter to restrict the number of concurrent requests. Profiles that are
    successfully fetched are returned in the resulting list.

    :param user_ids: A list of user IDs whose profiles need to be fetched.
    :type user_ids: list[int]
    :param user_fetcher: An instance of UserProfileFetcher that handles the
        fetching of user profiles.
    :type user_fetcher: UserProfileFetcher
    :return: A list of UserProfile instances that were successfully fetched.
        If a profile cannot be fetched or is unavailable, it will not be included
        in the returned list.
    :rtype: list[UserProfile]
    """
    global_rate_limiter = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    async def rate_limited_fetch(user_id):
        async with global_rate_limiter:
            return await user_fetcher.fetch_profile(user_id)

    tasks = [rate_limited_fetch(user_id) for user_id in user_ids]

    profiles: list[UserProfile] = []

    for result in asyncio.as_completed(tasks):
        profile = await result
        if profile is not None:
            profiles.append(profile)
            print(profile)

    return profiles


async def main():
    user_ids = list(_USER_PROFILES.keys())
    user_fetcher = UserProfileFetcher(
        _USER_PROFILES,
        failure_rate=0.3,
        min_delay=1.5,
        max_delay=3,
        rate_limit_per_second=10,
    )
    profiles = await fetch_user_profiles(user_ids, user_fetcher)

    print(f"Total profiles fetched: {len(profiles)}")
    print(f"Total errors: {len(user_ids) - len(profiles)}")
    print(f"Total retries: {user_fetcher.total_num_retries}")
    print(f"Average request time: {user_fetcher.average_request_time:.2f} seconds")

    for source, metrics in user_fetcher.source_metrics.items():
        print(
            f"Source: {source}, Success Rate: {metrics.success_rate:.2%}, "
            f"P50 Latency: {metrics.p50_latency:.2f} seconds, "
            f"P95 Latency: {metrics.p95_latency:.2f} seconds, "
            f"Total Requests: {metrics.num_requests}, "
            f"Total Retries: {metrics.num_retries}"
        )


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    asyncio.run(main())
