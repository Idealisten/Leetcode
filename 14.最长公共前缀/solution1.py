class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common = ""
        min_length = len(strs[0])
        for m in strs:
            if len(m) < min_length:
                min_length = len(m)
        for i in range(0, min_length):
            for j in range(0, len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return common
                else:
                    common = common + strs[j][i]


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
