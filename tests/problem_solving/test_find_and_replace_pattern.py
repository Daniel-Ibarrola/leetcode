from leetcode.problem_solving.find_and_replace_pattern import Solution


class TestFindAndReplacePattern:
    solution = Solution()

    def test_find_and_replace_multiple_patterns(self):
        assert self.solution.find_and_replace_pattern(
            ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"
        ) == ["mee", "aqq"]

    def test_find_and_replace_multiple_patterns_with_one_char(self):
        assert self.solution.find_and_replace_pattern(["a", "b", "c"], "a") == [
            "a",
            "b",
            "c",
        ]

    def test_no_pattern_matches(self):
        assert self.solution.find_and_replace_pattern(["abc", "deq"], "abb") == []

    def test_does_not_match_pattern(self):
        assert self.solution.match_pattern("abb", "ccc") is False
        assert self.solution.match_pattern("abb", "abc") is False

    def test_matches_pattern(self):
        assert self.solution.match_pattern("abb", "aqq") is True
        assert self.solution.match_pattern("abb", "mee") is True
