from leetcode.graphs.alien_dictionary import alien_order


def is_valid_order(result: str, words: list[str]) -> bool:
    """Check that result is consistent with the ordering implied by the word list."""
    position = {c: i for i, c in enumerate(result)}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if position[c1] >= position[c2]:
                    return False
                break
    return True


def test_simple_two_words():
    result = alien_order(["z", "x"])
    assert set(result) == {"z", "x"}
    assert is_valid_order(result, ["z", "x"])


def test_longer_example():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    result = alien_order(words)
    assert set(result) == {"w", "e", "r", "t", "f"}
    assert is_valid_order(result, words)


def test_cycle_returns_empty():
    # z > x and x > z is a contradiction
    assert alien_order(["z", "x", "z"]) == ""


def test_invalid_prefix_order_returns_empty():
    # "abc" before "ab" is impossible — longer word cannot precede its prefix
    assert alien_order(["abc", "ab"]) == ""


def test_single_word():
    result = alien_order(["abc"])
    assert set(result) == {"a", "b", "c"}


def test_all_same_words():
    result = alien_order(["abc", "abc"])
    assert set(result) == {"a", "b", "c"}


def test_no_ordering_constraints():
    # All words share the same first character — no edges can be derived
    result = alien_order(["a", "b", "c"])
    assert set(result) == {"a", "b", "c"}
    assert is_valid_order(result, ["a", "b", "c"])


def test_three_way_cycle_returns_empty():
    # a > b, b > c, c > a
    assert alien_order(["a", "b", "c", "a"]) == ""
