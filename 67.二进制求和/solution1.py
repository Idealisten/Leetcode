class Solution:
    def addBinary(self, a, b):
        if len(a) > len(b):
            #   将b的长度补齐到a的长度
            for i in range(0, len(a)-len(b)):
                b = "0" + b
        else:
            #   将a的长度补齐到b的长度
            for i in range(0, len(b) - len(a)):
                a = "0" + a
        #   将a和b都加一个前导0，预防最高位进位
        a = "0" + a
        b = "0" + b
        #   carry表示是否有进位
        carry = 0
        sum = []
        for i in range(len(a)-1, -1, -1):
            if (a[i] == "0") and (b[i] == "0"):
                if carry == 0:
                    sum.append("0")
                    carry = 0
                elif carry == 1:
                    sum.append("1")
                    carry = 0
            elif ((a[i] == "0") and (b[i] == "1")) or ((a[i] == "1") and (b[i] == "0")):
                if carry == 0:
                    sum.append("1")
                elif carry == 1:
                    sum.append("0")
                    carry = 1
            elif (a[i] == "1") and (b[i] == "1"):
                if carry == 0:
                    sum.append("0")
                    carry = 1
                elif carry == 1:
                    sum.append("1")
                    carry = 1
        sum.reverse()

        sum_str = "".join(sum)
        return str(int(sum_str))


s = Solution()
print(s.addBinary("1010", "1011"))

