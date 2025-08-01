class Solution:
    @staticmethod
    def triangle_number(nums: list[int]) -> int:
        """Returns the number of triplets in an array that can form a valid triangle

        :param nums: a list of integers representing the sides of a triangle
        :return: number of valid triplets
        """
        num_triplets = 0
        nums.sort()

        for ii in range(len(nums) - 1, 1, -1):
            left, right = 0, ii - 1

            while left < right:
                if nums[left] + nums[right] > nums[ii]:
                    num_triplets += right - left
                    right -= 1
                else:
                    left += 1

        return num_triplets
