def sort_by_parity(nums: list[int]) -> list[int]:
    even: list[int] = []
    odd: list[int] = []

    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even + odd


def sort_by_parity_2(nums: list[int]) -> list[int]:
    sorted_nums: list[int] = [0] * len(nums)
    even_index = 0
    odd_index = 1

    for num in nums:
        if num % 2 == 0:
            sorted_nums[even_index] = num
            even_index += 2
        else:
            sorted_nums[odd_index] = num
            odd_index += 2

    return sorted_nums
