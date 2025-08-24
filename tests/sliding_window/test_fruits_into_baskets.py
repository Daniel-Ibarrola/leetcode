import pytest
from leetcode.sliding_window.fruits_into_baskets import fruits_into_baskets


class TestFruitIntoBaskets:
    @pytest.mark.parametrize(
        "fruits, expected",
        [
            # Example cases
            ([1, 2, 1], 3),
            ([0, 1, 2, 2], 3),
            ([1, 2, 3, 2, 2], 4),
            # All same fruit type
            ([1, 1, 1, 1], 4),
            # Only two types, alternating
            ([1, 2, 1, 2, 1, 2], 6),
            # More than two types, longest valid is in middle
            ([1, 2, 3, 2, 2, 4, 5], 4),  # [2,3,2,2]
            # Only one fruit
            ([7], 1),
            # Decreasing pattern
            ([3, 3, 2, 1, 1], 3),  # [3,3,2,1] not valid (3 types), but [2,1,1] is valid
            # Start with two types then introduce third
            ([1, 2, 1, 3], 3),  # [1,2,1]
            # Complex pattern
            ([0, 1, 6, 6, 4, 4, 6], 5),  # [6,6,4,4,6]
            # Edge case: long stretch of one type followed by one more
            ([8] * 1000 + [9], 1001),
            # Edge case: long alternating
            ([1, 2] * 10000, 20000),
        ],
    )
    def test_total_fruit(self, fruits, expected):
        assert fruits_into_baskets(fruits) == expected
