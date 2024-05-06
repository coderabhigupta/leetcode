# 39. Combination Sum
# Link: https://leetcode.com/problems/combination-sum

class Solution:
    def __init__(self):
        self.candidates = []
        self.results = []

    def recursiveCombinationSum(self, start: int, target: int, combination: List[int]) -> List[int]:
        if target == 0:
            self.results.append(combination)
            return
        elif target < 0:
            return

        for i in range(start, len(self.candidates)):
            can = self.candidates[i]
            self.recursiveCombinationSum(i, target - can, combination + [can])

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.recursiveCombinationSum(0, target, [])
        return self.results