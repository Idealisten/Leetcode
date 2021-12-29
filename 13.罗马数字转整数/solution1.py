class Solution:
    def romanToInt(self, s: str) -> int:
        r = 0
        ne = 0
        for i in range(len(s)):
            if ne == 1:
                ne = 0
                continue
            else:
                if s[i] == "V":
                    r = r + 5
                elif s[i] == "L":
                    r = r + 50
                elif s[i] == "D":
                    r = r + 500
                elif s[i] == "M":
                    r = r + 1000
                elif s[i] == "I":
                    if i < len(s)-1:
                        if s[i+1] == "V":   # 检查是不是IV
                            r = r + 4
                            ne = 1
                        elif s[i+1] == "X":    # 检查是不是IX
                            r = r + 9
                            ne = 1
                        else:
                            r = r + 1
                    else:
                        r = r + 1
                elif s[i] == "X":
                    if i < len(s)-1:
                        if s[i+1] == "L":
                            r = r + 40
                            ne = 1
                        elif s[i+1] == "C":
                            r = r + 90
                            ne = 1
                        else:
                            r = r + 10
                    else:
                        r = r + 10
                elif s[i] == "C":
                    if i < len(s)-1:
                        if s[i+1] == "D":
                            r = r + 400
                            ne = 1
                        elif s[i+1] == "M":
                            r = r + 900
                            ne = 1
                        else:
                            r = r + 100
                    else:
                        r = r + 100
        return r


s = Solution()
print(s.romanToInt("III"))

