from math import inf

# Solution 1:
# Computes the sum for each possible interval of length k
# Not efficient enough - O(n * k)

class Solution1:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_total_so_far = -inf
        for i in range(len(nums) - k + 1):
            total = sum(nums[i:i + k])
            max_total_so_far = max(max_total_so_far, total)

        return max_total_so_far / k


# Solution 2:
# Sliding window (while loop, two indices)
# More efficient - O(n)

class Solution2:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i = 0  # Start of sliding window (inclusive)
        j = k  # End of sliding window (exclusive)

        window_total = sum(nums[i:j])
        max_total_so_far = window_total

        while j < len(nums):
            window_total += nums[j] - nums[i]

            i += 1
            j += 1

            max_total_so_far = max(max_total_so_far, window_total)

        return max_total_so_far / k


# Solution 3:
# Sliding window (for loop)
# Equivalent to Solution 2 - O(n)

class Solution3:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_total = sum(nums[:k])
        max_total_so_far = window_total

        for i in range(len(nums) - k):
            window_total += nums[i+k] - nums[i]
            max_total_so_far = max(max_total_so_far, window_total)

        return max_total_so_far / k



