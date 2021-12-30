class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        else:
            stack = ""
            k = -1
            for i in s:
                if i == "(" or i == "[" or i == "{":
                    stack = stack + i
                    k = k + 1
                else:
                    if (i == ")" or i == "]" or i == "}") and len(stack) == 0:
                        return False
                    else:
                        if (i == ")" and stack[len(stack)-1] == "(") or (i == "]" and stack[len(stack)-1] == "[") or (i == "}" and stack[len(stack)-1] == "{"):
                            k = k - 1
                            stack = stack[:-1]
                        else:
                            return False
            if len(stack) == 0:
                return True
            else:
                return False



s = Solution()
print(s.isValid("){"))

