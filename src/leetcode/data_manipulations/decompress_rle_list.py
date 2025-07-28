class Solution:
    @staticmethod
    def decompress_rle_list(nums: list[int]) -> list[int]:
        decompressed_list: list[int] = []
        for ii in range(0, len(nums), 2):
            freq, val = nums[ii], nums[ii + 1]
            decompressed_list.extend([val] * freq)

        return decompressed_list
