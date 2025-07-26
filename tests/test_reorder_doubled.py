import pytest

from leetcode.reorder_doubled import Solution


class TestReorderDoubled:

    solution = Solution()

    @pytest.mark.parametrize("arr", [[3, 1, 3, 6], [2, 1, 2, 6]])
    def test_returns_false_when_array_cannot_be_reordered(self, arr: list[int]):
        assert self.solution.can_reorder_doubled(arr) is False

    @pytest.mark.parametrize(
        "arr",
        [
            [4, -2, 2, -4],
            [1, 2, 4, 8],
            [-6, -3, 1, 2],
            [2, 4, 0, 0, 8, 1],
            [4, 8, 0, 0, 16, 2],
        ],
    )
    def test_returns_true_when_array_can_be_reordered(self, arr: list[int]):
        assert self.solution.can_reorder_doubled(arr) is True

    def test_when_array_is_empty(self):
        assert self.solution.can_reorder_doubled([]) is True

    def test_works_with_repeated_elements(self):
        assert self.solution.can_reorder_doubled([1, 2, 4, 16, 8, 4]) is False
