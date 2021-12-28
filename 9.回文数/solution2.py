class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            if x // 10 == 0:
                return True
            else:
                c = 0
                temp = x
                while True:
                    b = x // 10
                    a = x % 10
                    c = c*10 + a
                    x = int(x/10)
                    if b == 0:
                        break
                if c == temp:
                    return True
                else:
                    return False


s = Solution()
print(s.isPalindrome(121))
