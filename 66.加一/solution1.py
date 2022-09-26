class Solution:
    def plusOne(self, digits):
        sum = 0
        power = 1
        digits_new = []
        for i in range(len(digits)-1, -1, -1):
            digit = digits[i] * power
            sum += digit
            power = power * 10
        sum += 1
        #   通过余数将每一位加到列表里
        while sum != 0:
            remainder = sum % 10
            digits_new.insert(0, remainder)
            sum = sum // 10
        return digits_new


s = Solution()
print(s.plusOne([1, 2, 3]))
