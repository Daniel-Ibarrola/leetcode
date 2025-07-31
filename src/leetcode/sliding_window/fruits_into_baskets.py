def fruits_into_baskets(fruits: list[int]) -> int:
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
