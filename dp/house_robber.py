# 198. House Robber
# Link: https://leetcode.com/problems/house-robber

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = nums[0]
        rob2 = 0

        for num in nums[1:]:
            temp = rob1
            rob1 = max(rob2 + num, rob1)
            rob2 = temp

        return rob1
