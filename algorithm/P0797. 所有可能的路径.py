#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-02 16:29
FileName: algorithm
Description:P0797. 所有可能的路径.py 
"""
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(i, path):
            if i == len(graph) - 1:
                paths.append(path)
            for j in graph[i]:
                dfs(j, path + [j])

        paths = []
        dfs(0, [0])
        return paths


if __name__ == '__main__':
    print(Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
