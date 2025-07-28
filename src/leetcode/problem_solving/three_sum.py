from collections import Counter

MOD = 10**9 + 7


class Solution:

    @staticmethod
    def three_sum_with_multiplicity(arr: list[int], target: int) -> int:

        counts = Counter(arr)
        ans = 0

        # Get a sorted list of unique numbers to iterate over
        keys = sorted(counts.keys())

        for i, x in enumerate(keys):
            # We are looking for two other numbers y and z from the list
            # such that y + z = T, where T is the remaining target.
            T = target - x

            # Use a two-pointer approach on the rest of the keys
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]

                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else:  # y + z == T. Found a valid triplet of values.
                    # Now, calculate combinations based on the values.
                    if i < j < k:  # Case 1: x < y < z
                        ans += counts[x] * counts[y] * counts[z]
                    elif i == j < k:  # Case 2: x = y < z
                        ans += (counts[x] * (counts[x] - 1) // 2) * counts[z]
                    elif i < j == k:  # Case 3: x < y = z
                        ans += counts[x] * (counts[y] * (counts[y] - 1) // 2)
                    elif i == j == k:  # Case 4: x = y = z
                        ans += counts[x] * (counts[x] - 1) * (counts[x] - 2) // 6

                    # Move pointers to find the next unique pair
                    j += 1
                    k -= 1

        return ans % MOD
