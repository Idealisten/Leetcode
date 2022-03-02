#   逆向双指针，空间复杂度O(1)
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1
        b = n - 1
        c = m + n - 1
        while a >= 0 and b >= 0:
            if nums1[a] > nums2[b]:
                nums1[c] = nums1[a]
                c = c - 1
                a = a - 1
            elif nums1[a] < nums2[b]:
                nums1[c] = nums2[b]
                c = c - 1
                b = b - 1
            else:
                nums1[c] = nums2[b]
                c = c - 1
                b = b - 1
                nums1[c] = nums1[a]
                c = c - 1
                a = a - 1
        if a < 0:
            while b >= 0:
                nums1[c] = nums2[b]
                c = c - 1
                b = b - 1
        print(nums1)


s = Solution()
s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
