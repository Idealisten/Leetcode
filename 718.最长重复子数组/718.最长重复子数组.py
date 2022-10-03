"""
暴力解法
"""


class Solution:
    def findLength(self, nums1, nums2) -> int:
        ans = 0
        for i in range(len(nums1)):
            # print("i: {}".format(i))
            for j in range(len(nums2)):
                # print("j: {}".format(j))
                k = 0
                while i + k < len(nums1) and j + k < len(nums2) and nums1[i + k] == nums2[j + k]:
                    # print("k: {}".format(k))
                    k += 1

                ans = max(ans, k)
        return ans


s = Solution()
lens = s.findLength([0, 1, 1, 1, 1], [1, 0, 1, 0, 1])
print(lens)
