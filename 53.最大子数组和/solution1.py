#   贪心算法
#   如果当前指针所指元素之前的和小于0，则丢弃当前元素之前的数列

class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        sum = 0
        for i in range(len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum = sum + nums[i]
            if max_sum < sum:
                max_sum = sum
        return max_sum


s = Solution()
print(s.maxSubArray([1]))
