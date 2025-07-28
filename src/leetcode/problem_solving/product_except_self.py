class Solution:
    @staticmethod
    def product_except_self(nums: list[int]) -> list[int]:
        products = [1] * len(nums)

        for ii in range(len(products)):
            for jj in range(len(nums)):
                if ii != jj:
                    products[ii] *= nums[jj]

        return products
