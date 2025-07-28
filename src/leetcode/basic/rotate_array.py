class Solution:
    @staticmethod
    def rotate(nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotated: list[int] = [0] * len(nums)
        for ii in range(len(nums)):
            rotated[(ii + k) % len(nums)] = nums[ii]

        nums[:] = rotated[:]
