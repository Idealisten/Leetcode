class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 2))
