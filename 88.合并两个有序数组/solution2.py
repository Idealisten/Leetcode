#   正向双指针
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        a = 0
        b = 0
        small_len = len(nums1) if len(nums1) < len(nums2) else len(nums2)
        while a < m and b < n:
            if nums1[a] < nums2[b]:
                result.append(nums1[a])
                a = a + 1
            elif nums1[a] > nums2[b]:
                result.append(nums2[b])
                b = b + 1
            else:
                result.append(nums1[a])
                result.append(nums2[b])
                a = a + 1
                b = b + 1
        if b == len(nums2):
            result.extend(nums1[a:])
        else:
            result.extend(nums2[b:])
        for i in range(m+n):
            nums1[i] = result[i]
        print(nums1)


s = Solution()
s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

