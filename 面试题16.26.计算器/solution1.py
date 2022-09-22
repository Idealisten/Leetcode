class Solution:
    operator_stack = []
    operand_stack = []

    def calculate(self, s: str):
        i = 0
        lens = len(s)
        while i < lens:
            if s[i].isdigit() is True:
                j = 1
                num = s[i]
                x = i
                while j < lens - i:
                    if s[x+j].isdigit() is True:
                        num = num + s[x+j]
                        j = j + 1
                        i = i + 1
                    else:
                        break
                self.operand_stack.append(int(num))
                i = i + 1
                # 每个数字入栈后检查当前符号栈顶是否为*或/且优先级大于栈顶-1元素，如果是先计算

            else:
                self.operator_stack.append(s[i])
                i = i + 1
        # print(self.operator_stack)
        # print(self.operand_stack)


s = Solution()
s.calculate("23+5*80")
