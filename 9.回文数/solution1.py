class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            x_str = str(x)
            len_x = len(x_str)
            if len_x == 1:
                return True
            else:
                palindrome = 1
                for i in range(0, int(len_x/2)+1):
                    if x_str[i] != x_str[len_x-1-i]:
                        palindrome = 0
                        return False
                if palindrome == 1:
                    return True

