"""
动态规划
https://www.bilibili.com/video/BV1XS4y1G7rs/?spm_id_from=autoNext&vd_source=751d83a470a7b7086d96d8b5dd5762d9
"""
class Solution:
    def lengthOfLIS(self, heights: List[int]) -> int:
        nums = len(heights)
        left = [0 for i in range(nums)]

        for i in range(nums):
            left[i] = 1
            for ii in range(i):
                if heights[i] > heights[ii]:
                    left[i] = max(left[i], left[ii] + 1)

        return max(left)




