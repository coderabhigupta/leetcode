# 33. Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        minimum = nums[0]

        while low <= high:
            mid = (low + high) // 2
    
            if nums[mid] < minimum:
                minimum = nums[mid]
            
            if nums[high] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return minimum
              
