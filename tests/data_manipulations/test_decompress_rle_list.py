import pytest
from leetcode.data_manipulations.decompress_rle_list import (
    Solution,
)


class TestDecompressRLEList:
    solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            # Example 1
            ([1, 2, 3, 4], [2, 4, 4, 4]),
            # Example 2
            ([1, 1, 2, 3], [1, 3, 3]),
            # Single pair
            ([5, 7], [7, 7, 7, 7, 7]),
            # All frequencies are 1
            ([1, 10, 1, 20, 1, 30], [10, 20, 30]),
            # All values are the same
            ([3, 5, 2, 5], [5, 5, 5, 5, 5]),
            # Edge case: alternating freq/val
            ([2, 1, 1, 2, 3, 3], [1, 1, 2, 3, 3, 3]),
            # Maximum freq value
            ([100, 1], [1] * 100),
        ],
    )
    def test_decompress_rle_list(self, nums: list[int], expected: list[int]):
        assert self.solution.decompress_rle_list(nums) == expected
