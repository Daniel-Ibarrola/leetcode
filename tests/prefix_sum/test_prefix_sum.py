from leetcode.prefix_sum.prefix_sum import prefix_sums


class TestPrefixSum:

    def test_prefix_sums_has_the_sums_of_all_subarrays(self):
        arr = [1, 3, 4, 6, 2, 5, 8]
        expected = [0, 1, 4, 8, 14, 16, 21, 29]
        assert prefix_sums(arr) == expected

    def test_can_use_prefix_sums_to_find_the_sum_of_a_subarray(self):
        arr = [1, 3, 4, 6, 2, 5, 8]
        # sum between i = 3 and i = 5 must be 13
        prefix_sums_arr = prefix_sums(arr)
        assert prefix_sums_arr[6] - prefix_sums_arr[3] == 13
