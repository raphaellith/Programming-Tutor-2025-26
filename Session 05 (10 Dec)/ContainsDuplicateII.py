class Solution1:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        if k >= n:
            return len(set(nums)) < n

        # n > k
        nums_in_window = set(nums[:k + 1])
        if len(nums_in_window) < k + 1:
            return True

        for i in range(n - k - 1):
            nums_in_window.remove(nums[i])
            nums_in_window.add(nums[i + k + 1])

            if len(nums_in_window) < k + 1:
                return True

        return False


class Solution2:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        nums_in_window = set()

        for i in range(len(nums)):
            if i > k:
                nums_in_window.remove(nums[i - k - 1])

            if nums[i] in nums_in_window:
                return True

            nums_in_window.add(nums[i])

        return False


class Solution3:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Key: integer in nums
        # Value: Most recent index of integer
        most_recent_index_of_nums = dict()

        for i in range(len(nums)):
            if nums[i] in most_recent_index_of_nums and abs(most_recent_index_of_nums[nums[i]] - i) <= k:
                return True

            most_recent_index_of_nums[nums[i]] = i

        return False
