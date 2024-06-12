# 189. Rotate Array
# Link: https://leetcode.com/problems/rotate-array/description/

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n == 1: return

        if k >= n:
            k %= n

        if k == 0: return

        for i in range((n-k)//2):
            nums[i], nums[n-k-i-1] = nums[n-k-i-1], nums[i]

        nums.reverse()

        for i in range(k//2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]

