# 双指针
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        else:
            slow = 0
            fast = 1
            while fast < len(nums):
                if nums[fast] == nums[slow]:
                    fast += 1
                else:
                    nums[slow+1] = nums[fast]
                    slow += 1
                    fast += 1
            nums = nums[0:slow+1]
            print(nums)
            return slow+1


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
