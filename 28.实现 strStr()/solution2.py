# KMP算法
class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        next = []
        next.append(0)
        x = 1   # 模式串中依次遍历的下标
        now = 0  # 模式串中要获得next[x]而和p[x]比较的字符的下标
        while x < len(needle):
            if needle[x] == needle[now]:
                now += 1
                x += 1
                next.append(now)
            elif now != 0:
                now = next[now-1]
            else:
                next.append(0)
                x += 1
        m = 0   # 主串即将要匹配的下标
        p = 0   # 模式串即将要匹配的下标
        while m < len(haystack):
            if haystack[m] == needle[p]:    # 如果两个字符相等，则主串和模式串下标分别进一位
                m += 1
                p += 1
            elif p != 0:    # 如果没匹配上，并且模式串要匹配的字符下标不为0，则根据next数组移动模式串
                p = next[p-1]
            else:   # 如果没匹配上，且要匹配的是模式串的第一个字符，则直接把模式串右移一位，匹配主串的下一个字符
                m += 1
            if p == len(needle):
                return m - p
        return -1





