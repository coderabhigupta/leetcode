# 1684. Count the Number of Consistent Strings
# Link: https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set()

        for c in allowed:
            if c not in s:
                s.add(c)

        count = len(words)

        for word in words:
            for c in word:
                if c not in s:
                    count -= 1
                    break

        return count
