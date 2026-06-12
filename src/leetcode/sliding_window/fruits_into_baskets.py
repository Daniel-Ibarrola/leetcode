def fruits_into_baskets(fruits: list[int]) -> int:
    """
    Calculate the maximum number of fruits you can collect from an integer array fruits,
    where each element represents a type of fruit.

    You can start collecting fruits from any position in the array,
    but you must stop once you encounter a third distinct type of fruit.

    The goal is to find the longest subarray where at most two different types of fruits are collected.
    """
    state: dict[int, int] = {}
    current_max = 0
    start = 0
    for end in range(len(fruits)):
        fruit = fruits[end]
        state[fruit] = state.get(fruit, 0) + 1

        while len(state) > 2:
            state[fruits[start]] -= 1
            if state[fruits[start]] == 0:
                del state[fruits[start]]
            start += 1

        current_max = max(current_max, end - start + 1)
    return current_max
