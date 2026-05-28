from leetcode.concurrency.asyncio import web_crawler

_USER_PROFILES: dict[int, web_crawler.UserProfile] = {
    1: web_crawler.UserProfile(1, "facebook", "John Doe"),
    2: web_crawler.UserProfile(2, "twitter", "Jane Doe"),
    3: web_crawler.UserProfile(3, "linkedin", "Bob Smith"),
}


async def test_fetch_user_profiles():

    user_ids = [1, 2, 3]
    user_fetcher = web_crawler.UserProfileFetcher(_USER_PROFILES, 0, 0, 0)
    user_data = await web_crawler.fetch_user_profiles(user_ids, user_fetcher)

    assert user_data == list(_USER_PROFILES.values())
