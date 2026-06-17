from collections import defaultdict, deque


def alien_order(words: list[str]) -> str:
    """
    There is a foreign language which uses the latin alphabet, but the order
    among letters is not "a", "b", "c" ... "z" as in English.

    You receive a list of non-empty strings words from the dictionary, where
    the words are sorted lexicographically by the rules of this new language.

    Derive the order of letters in this language and return it as a string.
    If the order is invalid (i.e. a cycle exists), return "".
    If there are multiple valid orderings, return any of them.

    Example 1:
        Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
        Output: "wertf"

    Example 2:
        Input: words = ["z", "x"]
        Output: "zx"

    Example 3:
        Input: words = ["z", "x", "z"]
        Output: ""
        Explanation: The order is invalid, so return "".

    Example 4:
        Input: words = ["abc", "ab"]
        Output: ""
        Explanation: "abc" comes before "ab" but "abc" is longer — impossible.

    Constraints:
        - 1 <= words.length <= 100
        - 1 <= words[i].length <= 100
        - words[i] consists of only lowercase English letters
    """
    graph: dict[str, set[str]] = defaultdict(set)
    unique_chars: set[str] = {c for word in words for c in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        for j in range(min_len):
            if w1[j] != w2[j]:
                graph[w1[j]].add(w2[j])
                break
        else:
            if len(w1) > len(w2):
                return ""

    indegree: dict[str, int] = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque([u for u in unique_chars if indegree[u] == 0])
    topological_order: list[str] = []

    while len(queue) > 0:
        node = queue.popleft()
        topological_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topological_order) != len(unique_chars):
        return ""

    return "".join(topological_order)
