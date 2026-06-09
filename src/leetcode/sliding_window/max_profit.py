def max_profit(prices: list[int]) -> int:
    current_max = 0
    left = 0

    for right in range(1, len(prices)):

        if prices[right] > prices[left]:
            current_max = max(current_max, prices[right] - prices[left])
        else:
            left = right

    return current_max
