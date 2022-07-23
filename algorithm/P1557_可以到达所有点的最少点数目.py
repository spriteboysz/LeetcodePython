#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 13:50:59
LastEditTime: 2022-03-19 13:54:42
Description: 
FilePath: 1557.可以到达所有点的最少点数目.py
"""
#
# @lc app=leetcode.cn id=1557 lang=python3
#
# [1557] 可以到达所有点的最少点数目
#

# @lc code=start
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes, tos = [i for i in range(n)], [to for _, to in edges]
        return list(set(nodes) - set(tos))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findSmallestSetOfVertices(
        n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    )
    print(ans)
    ans = solution.findSmallestSetOfVertices(
        n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    )
    print(ans)
