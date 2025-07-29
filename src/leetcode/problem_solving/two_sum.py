class Solution:

    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for ii in range(len(nums)):
            complement = target - nums[ii]
            if complement in seen:
                return [seen[complement], ii]
            seen[nums[ii]] = ii

        raise ValueError("No pair found")
