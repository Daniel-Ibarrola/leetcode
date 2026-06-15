def subsets(nums: list[int]) -> list[list[int]]:
    """
    Given an integer array nums of unique elements, return all possible subsets that can be made from the elements in nums.
    The solution set must not contain duplicate subsets, and the subsets can be returned in any order.
    """
    all_sets: list[list[int]] = []

    def dfs(index: int, current_subset: list[int]):
        if index == len(nums):
            all_sets.append(current_subset.copy())
            return

        # include element
        current_subset.append(nums[index])
        dfs(index + 1, current_subset)

        # exclude element
        current_subset.pop()
        dfs(index + 1, current_subset)

    dfs(0, [])
    return all_sets
