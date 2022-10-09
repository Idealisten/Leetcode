"""
滑动窗口方法，上短下长，从左向右滑动下方较长字符串
分为三个阶段：
1.重合长度小于较短字符串
2.重合长度等于较短字符串
3.重合长度再次小于较短字符串
三个阶段分别将重合部分从左向右扫描，字符相同count计数+1同时判断count是否大于最大相同值max_len，
不相同时将count归0，在下一位重新进行判断
三个阶段都扫描完成后返回最大值
"""


class Solution:
    def findLength(self, nums1, nums2) -> int:
        max_len = 0
        # 短的(len1)不动滑动长的(len2)
        if len(nums1) > len(nums2):
            t = nums1
            nums1 = nums2
            nums2 = t
        print("nums1:{}".format(nums1))
        print("nums2:{}".format(nums2))
        len1 = len(nums1)
        len2 = len(nums2)
        len_con = 1     # 重合部分长度

        while len_con < len1:
            sub_nums1 = nums1[0:len_con]
            sub_nums2 = nums2[len2 - len_con:len2]
            print("len_con:{}".format(len_con))
            print("sub_nums1:{}".format(sub_nums1))
            print("sub_nums2:{}".format(sub_nums2))
            count = 0
            for i in range(len_con):
                if sub_nums1[i] == sub_nums2[i]:
                    count += 1
                    print("count:{}".format(count))
                    if count > max_len:
                        max_len = count
                        print("max_len:{}".format(max_len))
                else:
                    max_len = max(count, max_len)
                    count = 0
            len_con += 1

        mo = 0
        while len_con + mo <= len2:
            sub_nums1 = nums1
            sub_nums2 = nums2[len2 - len1 - mo:len2 - mo]
            print("len_con:{}".format(len_con))
            print("sub_nums1:{}".format(sub_nums1))
            print("sub_nums2:{}".format(sub_nums2))
            count = 0
            for i in range(len_con):
                if sub_nums1[i] == sub_nums2[i]:
                    count += 1
                    print("count:{}".format(count))
                    if count > max_len:
                        max_len = count
                        print("max_len:{}".format(max_len))
                else:
                    max_len = max(count, max_len)
                    count = 0
            mo += 1

        while len_con >= 1:
            sub_nums1 = nums1[len1 - len_con:len1]
            sub_nums2 = nums2[0:0 + len_con]
            print("len_con:{}".format(len_con))
            print("sub_nums1:{}".format(sub_nums1))
            print("sub_nums2:{}".format(sub_nums2))
            count = 0
            for i in range(len_con):
                if sub_nums1[i] == sub_nums2[i]:
                    count += 1
                    print("count:{}".format(count))
                    if count > max_len:
                        max_len = count
                        print("max_len:{}".format(max_len))
                else:
                    max_len = max(count, max_len)
                    count = 0
            len_con -= 1

        return max_len


s = Solution()
print(s.findLength([1, 1, 1, 1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
