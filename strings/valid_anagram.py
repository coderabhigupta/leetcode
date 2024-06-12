# 242. Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1


        for c in t:
            if c not in m:
                return False
            
            m[c] -= 1
            if m[c] == 0:
                del m[c]
        
        return len(m.keys()) == 0
