class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common = ""
        min_length = len(strs[0])
        if len(strs) == 1:
            return strs[0]
        else:
            for m in strs:
                if len(m) < min_length:
                    min_length = len(m)
            for i in range(0, min_length):
                flag = 1
                for j in range(1, len(strs)):
                    if strs[j][i] != strs[0][i]:
                        flag = 0
                        return common
                if flag == 1:
                    common = common + strs[j][i]
            return common


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight", "f"]))
