# 1143. Longest Common Subsequence
# Link: https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        matrix = [[0] * (n + 1) for _ in range(m + 1)]

        for j in reversed(range(0, n)):
            for i in reversed(range(0, m)):
                if text1[i] == text2[j]:
                    matrix[i][j] = matrix[i + 1][j + 1] + 1
                else:
                    matrix[i][j] = max(matrix[i + 1][j], matrix[i][j + 1])

        return matrix[0][0]
