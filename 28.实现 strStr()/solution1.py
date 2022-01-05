class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1
        else:
            e = 1
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    e = 0
                    for j in range(0, len(needle)):
                        if i+j >= len(haystack):
                            return -1
                        else:
                            if needle[j] != haystack[i+j]:
                                if i + len(needle) == len(haystack):
                                    return -1
                                else:
                                    break
                            if j == len(needle)-1:
                                if needle[j] == haystack[i+j]:
                                    return i
                else:
                    if i + len(needle) == len(haystack):
                        return -1
            if e == 1:
                return -1


s = Solution()
print(s.strStr("baaaaaaaa", "bagytisyy"))
