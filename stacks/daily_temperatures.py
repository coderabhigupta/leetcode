# 739. Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, idx = stack.pop()
                ans[idx] = i - idx

            stack.append((t, i))

        return ans