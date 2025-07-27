class Solution:
    @staticmethod
    def count_occurrences(nums: list[int], queries: list[int], x: int) -> list[int]:
        query_results = []

        x_occurrences: list[int] = []
        for ii in range(len(nums)):
            if nums[ii] == x:
                x_occurrences.append(ii)

        for required_occurrence in queries:
            if required_occurrence > len(x_occurrences):
                query_results.append(-1)
            else:
                query_results.append(x_occurrences[required_occurrence - 1])

        return query_results
