import pytest
from leetcode.basic.maximum_wealth import Solution


class TestRichestCustomer:
    solution = Solution()

    @pytest.mark.parametrize(
        "accounts, expected",
        [
            # Example cases
            ([[1, 2, 3], [3, 2, 1]], 6),
            ([[1, 5], [7, 3], [3, 5]], 10),
            ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
            # Single customer
            ([[10, 10, 10]], 30),
            # Multiple customers, increasing wealth
            ([[1, 1], [2, 2], [3, 3], [4, 4]], 8),
            # All have same wealth
            ([[5, 5], [5, 5], [5, 5]], 10),
            # Wealth concentrated in one account
            ([[0, 0], [100, 0], [0, 100], [99, 1]], 100),
            # Edge case: Minimum values
            ([[1]], 1),
            # Edge case: All accounts have 1
            ([[1] * 50 for _ in range(50)], 50),
        ],
    )
    def test_maximum_wealth(self, accounts, expected):
        assert self.solution.maximum_wealth(accounts) == expected
