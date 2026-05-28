import asyncio
import dataclasses
import time
from typing import Optional
import random
import logging


@dataclasses.dataclass
class UserProfile:
    user_id: int
    source: str
    name: str


_USER_PROFILES: dict[int, UserProfile] = {
    1: UserProfile(1, "facebook", "John Doe"),
    2: UserProfile(2, "twitter", "Jane Doe"),
    3: UserProfile(3, "linkedin", "Bob Smith"),
    4: UserProfile(4, "github", "Alice Johnson"),
    5: UserProfile(5, "instagram", "Emily Davis"),
    6: UserProfile(6, "reddit", "Michael Brown"),
    7: UserProfile(7, "tiktok", "Sophia Wilson"),
    8: UserProfile(8, "youtube", "David Lee"),
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
        self._rate_limit_per_second = rate_limit_per_second
        self._max_retries = max_retries
        self._total_num_retries = 0
        self._request_times: list[float] = []

    @property
    def total_num_retries(self) -> int:
        return self._total_num_retries

    @property
    def average_request_time(self) -> float:
        if not self._request_times:
            return 0.0
        return sum(self._request_times) / len(self._request_times)

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
        logging.info("Fetching user profile for user_id %s", user_id)

        start_time = time.perf_counter()

        sleep_time = random.uniform(self._min_delay, self._max_delay)
        logging.info("Delay %s seconds", sleep_time)

        await asyncio.sleep(sleep_time)

        if random.random() < self._failure_rate:
            logging.error("Failed to fetch user profile for user_id %s", user_id)
            raise FetchError(f"Failed to fetch user profile for user_id {user_id}")

        end_time = time.perf_counter()
        self._request_times.append(end_time - start_time)

        return self._user_profiles.get(user_id)

    async def _fetch_with_retry(self, user_id):
        """
        Fetch user profile with exponential backoff retry mechanism.
        """
        sleep_time_on_failure = 0.1
        for attempt in range(self._max_retries):
            try:
                return await asyncio.wait_for(
                    self._call_user_api(user_id), timeout=TIMEOUT_SECONDS
                )
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
                        "Max retries reached for user_id %s. Skipping...", user_id
                    )
                    return None
        return None

    async def fetch_profile(self, user_id: int) -> Optional[UserProfile]:
        return await self._fetch_with_retry(user_id)


async def fetch_user_profiles(user_ids: list[int], user_fetcher: UserProfileFetcher):

    global_rate_limiter = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    async def rate_limited_fetch(user_id):
        async with global_rate_limiter:
            return await user_fetcher.fetch_profile(user_id)

    tasks = [rate_limited_fetch(user_id) for user_id in user_ids]

    num_errors = 0
    num_profiles = 0

    for result in asyncio.as_completed(tasks):
        profile = await result
        if profile is None:
            num_errors += 1
        else:
            num_profiles += 1
            print(profile)

    print(f"Total profiles fetched: {num_profiles}")
    print(f"Total errors: {num_errors}")
    print(f"Total retries: {user_fetcher.total_num_retries}")
    print(f"Average request time: {user_fetcher.average_request_time:.2f} seconds")


async def main():
    user_ids = list(_USER_PROFILES.keys())
    user_fetcher = UserProfileFetcher(
        _USER_PROFILES, failure_rate=0.3, min_delay=1.5, max_delay=3
    )
    await fetch_user_profiles(user_ids, user_fetcher)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    asyncio.run(main())
