from leetcode.two_pointers.two_sum import has_pair_sum


class TestTwoSum:

    def test_has_pair_sum(self):
        assert has_pair_sum([1, 3, 4, 6, 8, 10, 13], 13) is True

    def test_does_not_have_pair_sum(self):
        assert has_pair_sum([1, 3, 4, 6, 8, 10, 13], 6) is False
