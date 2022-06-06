#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-06 23:57
LastEditTime: 2022-06-06 23:57
Description:
FilePath: 剑指 Offer II 110. 所有路径.py
"""

from typing import List
from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths, queue = [], deque([[0]])
        while queue:
            cur = queue.popleft()
            for k in graph[cur[-1]]:
                if k == len(graph) - 1:
                    paths.append(cur + [len(graph) - 1])
                else:
                    queue.append(cur + [k])
        return paths


if __name__ == '__main__':
    solution = Solution()
    ans = solution.allPathsSourceTarget(
        graph=[[4, 3, 1], [3, 2, 4], [3], [4], []])
    print(ans)
    ans = solution.allPathsSourceTarget(graph=[[1], []])
    print(ans)
    ans = solution.allPathsSourceTarget(graph=[[1, 2, 3], [2], [3], []])
    print(ans)
    ans = solution.allPathsSourceTarget(graph=[[1, 3], [2], [3], []])
    print(ans)
