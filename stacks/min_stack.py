# 155. Min Stack
# Link: https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.stack.pop():
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


ms = MinStack()
ms.push(-1)
ms.push(0)
assert ms.getMin() == -1
ms.push(-2)
assert ms.top() == -2
ms.push(1)
assert ms.getMin() == -2
ms.push(-3)
assert ms.getMin() == -3
assert ms.top() == -3
ms.pop()
assert ms.getMin() == -2