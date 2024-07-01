# 1381. Design a Stack With Increment Operation
# Link: https://leetcode.com/problems/daily-temperatures

from typing import List


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack):
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        s = []

        while len(self.stack):
            s.append(self.stack.pop())

        while k and s:
            self.stack.append(s.pop() + val)
            k -= 1

        while s:
            self.stack.append(s.pop())

        print(self.stack)

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
