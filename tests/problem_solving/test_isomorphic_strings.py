from leetcode.problem_solving.isomorphic_strings import Solution


class TestIsomorphismStrings:

    solution = Solution()

    def test_is_isomorphic(self):
        assert self.solution.is_isomorphic("egg", "add") is True
        assert self.solution.is_isomorphic("paper", "title") is True

    def test_is_not_isomorphic(self):
        assert self.solution.is_isomorphic("foo", "bar") is False

    def test_different_order_of_characters(self):
        assert self.solution.is_isomorphic("bbbaaaba", "aaabbbba") is False

    def test_same_characters_twice(self):
        assert self.solution.is_isomorphic("abb", "abb") is True
