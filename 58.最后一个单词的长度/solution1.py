class Solution:
    def lengthOfLastWord(self, s: str):
        sum = 0
        find = False
        for i in range(len(s)-1, -1, -1):
            if i > 0:
                if s[i] == " ":
                    if find is False:
                        continue
                    else:
                        return sum
                if s[i] != " ":
                    find = True
                    sum += 1
            else:
                if s[i] == " ":
                    return sum
                else:
                    return sum+1
        return 1


s = Solution()
print(s.lengthOfLastWord("day"))


