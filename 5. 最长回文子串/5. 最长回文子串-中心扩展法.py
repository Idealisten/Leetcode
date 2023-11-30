class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0
        # 第一种情况，回文串长度为奇数
        for i in range(len(s)):
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    res = s[left:right+1]
            else:
                left += 1
                right -= 1
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    res = s[left:right+1]

        # 第二种情况，回文串长度为偶数
        for i in range(len(s)):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    res = s[left:right+1]
            else:
                left += 1
                right -= 1
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    res = s[left:right+1]
        return res