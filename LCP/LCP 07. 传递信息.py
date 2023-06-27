#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-14 23:33
LastEditTime: 2022-06-14 23:33
Description:
FilePath: LCP 07. 传递信息.py
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        adj = defaultdict(set)
        for x, y in relation:
            adj[x].add(y)

        queue, step = deque([0]), 0
        while queue and step < k:
            for _ in range(len(queue)):
                x = queue.popleft()
                for y in adj[x]:
                    queue.append(y)
            step += 1

        return queue.count(n - 1)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.numWays(
        n=5, relation=[
            [0, 2], [2, 1], [3, 4], [2, 3], [1, 4],
            [2, 0], [0, 4]], k=3)
    print(ans)
    ans = solution.numWays(n=3, relation=[[0, 2], [2, 1]], k=2)
    print(ans)
