# 150. Evaluate Reverse Polish Notation
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation

from typing import List

class Solution:
    def evaluate(self, op1, op2, oper) -> int:
        expr = 0

        if oper == '+':
            expr = op1 + op2
        elif oper == '-':
            expr = op1 - op2
        elif oper == '*':
            expr = op1 * op2
        else:
            expr = abs(op1) // abs(op2)

            if (op1 < 0 and op2 > 0) or (op2 < 0 and op1 > 0):
                expr = -expr

        return expr

    def evalRPN(self, tokens: List[str]) -> int:
        self.operands = []

        for t in tokens:
            if t in ['+', '-', '*', '/']:
                op2 = int(self.operands.pop())
                op1 = int(self.operands.pop())
                self.operands.append(self.evaluate(op1, op2, t))
            else:
                self.operands.append(int(t))

        return self.operands[-1]