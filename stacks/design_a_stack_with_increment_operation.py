# 1381. Design a Stack With Increment Operation
# Link: https://leetcode.com/problems/daily-temperatures

from typing import List


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.incr = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.incr.append(0)

    def pop(self) -> int:
        if len(self.stack):
            return self.stack.pop() + self.incr.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))

        for i in range(k):
            self.incr[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
