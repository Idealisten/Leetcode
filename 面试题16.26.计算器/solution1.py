class Solution:
    operator_stack = []
    operand_stack = []

    def get_precedence(self, cur_op):
        stack_top = self.operator_stack.pop()
        self.operator_stack.append(stack_top)
        if stack_top == "*" or stack_top == "/":
            return True
        else:
            if cur_op == "+" or cur_op == "-":
                return True
            else:
                return False

    def calculate(self, s):
        s = s.replace(' ', '')
        i = 0
        lens = len(s)
        while i < lens:
            # 是数字
            if s[i].isdigit() is True:
                j = 1
                num = s[i]
                x = i   # 记录当前坐标位置，在此位置基础上+j判断是否为连续数字
                while j < lens - x:
                    if s[x+j].isdigit() is True:
                        num = num + s[x+j]
                        j = j + 1
                        i = i + 1
                    else:
                        break
                self.operand_stack.append(int(num))
                i = i + 1
            # 是运算符
            else:
                if len(self.operator_stack) == 0:   # 运算符栈空，直接入栈
                    self.operator_stack.append(s[i])
                else:
                    # 运算符栈非空时，循环取运算符栈栈顶运算符与当前运算符比较，把当前运算符之前所有能算顶都算了
                    while len(self.operator_stack) > 0:
                        cur_operator = s[i]
                        # 栈顶运算符优先级大于等于当前运算符优先级，运算后结果入栈
                        if self.get_precedence(cur_operator):
                            b = self.operand_stack.pop()
                            a = self.operand_stack.pop()
                            c = self.operator_stack.pop()
                            if c == "+":
                                d = a + b
                            elif c == "-":
                                d = a - b
                            elif c == "*":
                                d = a * b
                            else:
                                d = a // b
                            self.operand_stack.append(d)
                        else:
                            # 运算符优先级不满足，无需继续计算，跳出循环
                            break
                    self.operator_stack.append(s[i])
                    # 栈顶运算符优先级小于当前运算符优先级，运算符直接入栈

                i = i + 1
        while len(self.operator_stack) > 0:
            b = self.operand_stack.pop()
            a = self.operand_stack.pop()
            c = self.operator_stack.pop()
            if c == "+":
                d = a + b
            elif c == "-":
                d = a - b
            elif c == "*":
                d = a * b
            else:
                d = a // b
            self.operand_stack.append(d)
        return self.operand_stack.pop()
        # print(self.operator_stack)
        # print(self.operand_stack)


s = Solution()
print(s.calculate("1*2-3/4+5*6-7*8+9/10"))
