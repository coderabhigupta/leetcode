# 213. House Robber II
# Link: https://leetcode.com/problems/house-robber-ii

from typing import List

class Solution:
    def rob_n(self, nums: List[int]):
        rob1 = nums[0]
        rob2 = 0

        for num in nums[1:]:
            rob1, rob2  = max(rob2 + num, rob1), rob1
        
        return rob1

    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        
        if len(nums) == 1: return nums[0]

        return max(self.rob_n(nums[1:]), self.rob_n(nums[:-1]))

        
