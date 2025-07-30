class Solution:
    @staticmethod
    def maximum_wealth(accounts: list[list[int]]) -> int:
        max_wealth = 0
        for customer_accounts in accounts:
            max_wealth = max(max_wealth, sum(customer_accounts))

        return max_wealth
