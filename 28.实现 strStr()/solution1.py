class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            r = True
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    r = False
                    break
            if r is True:
                return i
        return -1


s = Solution()
print(s.strStr("a", "a"))
