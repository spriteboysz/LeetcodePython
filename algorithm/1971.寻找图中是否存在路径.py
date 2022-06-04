#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 10:19
LastEditTime: 2022-06-04 10:19
Description:
FilePath: 1971.寻找图中是否存在路径.py
"""

from typing import List


class Solution:
    def validPath(self,
                  n: int,
                  edges: List[List[int]],
                  source: int,
                  destination: int) -> bool:
        p = [i for i in range(n)]

        def get_root(node):
            if p[node] == node:
                return p[node]
            p[node] = get_root(p[node])
            return p[node]

        def merge(a, b):
            root_a, root_b = get_root(a), get_root(b)
            if root_a != root_b:
                p[root_a] = root_b

        for a, b in edges:
            merge(a, b)
        return get_root(source) == get_root(destination)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.validPath(
        n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)
    print(ans)
    ans = solution.validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [
                             5, 4], [4, 3]], source=0, destination=5)
    print(ans)
