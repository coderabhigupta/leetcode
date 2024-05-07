# 658. Find K Closest Elements
# Link: https://leetcode.com/problems/find-k-closest-elements/description/

import heapq
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for a in arr:
            delta = abs(a - x)
            heapq.heappush(heap, (-delta, -a))

            if len(heap) > k:
                heapq.heappop(heap)

        op = []
        while heap:
            op.append(-heapq.heappop(heap)[1])

        return sorted(op)