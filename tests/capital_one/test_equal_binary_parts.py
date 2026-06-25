from leetcode.capital_one.equal_binary_parts import can_divide_into_equal_parts


class TestCanDivideIntoEqualParts:

    def test_all_zeros(self):
        assert can_divide_into_equal_parts([0, 0, 0]) is True

    def test_valid_split(self):
        # [1,0], [1,0], [1] → 2, 2, 1 — not equal
        # [1], [0,1], [0,1] → 1, 1, 1 — equal
        assert can_divide_into_equal_parts([1, 0, 1, 0, 1]) is True

    def test_ones_not_divisible_by_three(self):
        assert can_divide_into_equal_parts([1, 1, 0, 1, 1]) is False

    def test_single_one_each(self):
        assert can_divide_into_equal_parts([0, 1, 0, 0, 1, 0, 0, 1, 0]) is True

    def test_impossible_due_to_trailing_zeros(self):
        # Each third must end with the same number of trailing zeros
        assert can_divide_into_equal_parts([1, 1, 0]) is False

    def test_all_ones(self):
        assert can_divide_into_equal_parts([1, 1, 1]) is True
