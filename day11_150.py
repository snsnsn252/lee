# 150
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(i)
            else:
                num2 = int(stack.pop()) # pay attention: int
                num1 = int(stack.pop()) # pay attention: int
                if i == "+":
                    res = num1 + num2
                elif i == "-":
                    res = num1 - num2
                elif i == "*":
                    res = num1 * num2
                else:
                    res = num1 / num2
                stack.append(res)
            
        return int(stack.pop()) # pay attention: int

