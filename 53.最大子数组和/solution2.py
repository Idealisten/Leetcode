#   动态规划算法
#   若前一个元素大于0(前一个元素是在动态变化的)，则将其加到当前元素上

class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        else:
            sum_max = nums[0]
            for i in range(1, len(nums)):
                if nums[i - 1] > 0:
                    nums[i] = nums[i] + nums[i-1]
                if nums[i] > sum_max:
                    sum_max = nums[i]
            return sum_max


s = Solution()
print(s.maxSubArray([5, 4, -1, 7, 8]))
