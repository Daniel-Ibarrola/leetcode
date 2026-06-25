from leetcode.capital_one.closest_sum_to_zero import closest_sum_to_zero


class TestClosestSumToZero:

    def test_exact_zero(self):
        assert closest_sum_to_zero([-3, -1, 1, 2]) == (-1, 1)

    def test_exact_zero_larger(self):
        assert closest_sum_to_zero([-5, -4, -3, 3, 7]) == (-3, 3)

    def test_all_positive(self):
        assert closest_sum_to_zero([1, 2, 3]) == (1, 2)

    def test_all_negative(self):
        assert closest_sum_to_zero([-5, -4, -3, -1]) == (-3, -1)

    def test_two_elements(self):
        assert closest_sum_to_zero([-1, 1]) == (-1, 1)

    def test_result_is_ordered(self):
        result = closest_sum_to_zero([-3, -1, 1, 2])
        assert result[0] < result[1]
