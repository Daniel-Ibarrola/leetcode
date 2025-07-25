class Solution:
    """
    Given four integer arrays nums1, nums2, nums3, and nums4 all length n, return the number of tuples (i, j, k, l) such that:

    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
    """

    @staticmethod
    def four_sum_count(
        nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:

        num_tuples = 0
        for ii in range(len(nums1)):
            for jj in range(len(nums2)):
                for kk in range(len(nums3)):
                    for ll in range(len(nums4)):
                        if nums1[ii] + nums2[jj] + nums3[kk] + nums4[ll] == 0:
                            num_tuples += 1

        return num_tuples
