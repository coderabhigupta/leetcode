# 934. Shortest Bridge
# Link: https://leetcode.com/problems/shortest-bridge

from typing import List

class Solution:
    def dfs(self, grid: List[List[int]], n: int, i: int, j: int, bfs_queue: List[int]):
        if i < 0 or j < 0 or i == n or j == n or grid[i][j] != 1:
            return

        grid[i][j] = 2
        bfs_queue.append((i, j))

        self.dfs(grid, n, i + 1, j, bfs_queue)
        self.dfs(grid, n, i - 1, j, bfs_queue)
        self.dfs(grid, n, i, j + 1, bfs_queue)
        self.dfs(grid, n, i, j - 1, bfs_queue)


    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        bfs_queue = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, n, i, j, bfs_queue)
                    break
            if bfs_queue:
                break

        distance = 0
        while bfs_queue:
            new_bfs_queue = []
            for i, j in bfs_queue:
                for nei_x, nei_y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= nei_x < n and 0 <= nei_y < n:
                        if grid[nei_x][nei_y] == 1:
                            return distance
                        else:
                            grid[nei_x][nei_y] = -1
                            new_bfs_queue.append((nei_x, nei_y))

            distance += 1
            bfs_queue = new_bfs_queue

        return distance
