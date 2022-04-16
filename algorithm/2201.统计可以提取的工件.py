#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-15 23:58:43
LastEditTime: 2022-04-16 00:04:15
Description: 
FilePath: 2201.统计可以提取的工件.py
"""
#
# @lc app=leetcode.cn id=2201 lang=python3
#
# [2201] 统计可以提取的工件
#

# @lc code=start
from typing import List


class Solution:
    def digArtifacts(
        self, n: int, artifacts: List[List[int]], dig: List[List[int]]
    ) -> int:
        matrix = [[False] * n for _ in range(n)]
        for i, j in dig:
            matrix[i][j] = True
        count = 0
        for x1, y1, x2, y2 in artifacts:
            flag = True
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if not matrix[i][j]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.digArtifacts(
        n=2, artifacts=[[0, 0, 0, 0], [0, 1, 1, 1]], dig=[[0, 0], [0, 1]]
    )
    print(ans)
    ans = solution.digArtifacts(
        n=2, artifacts=[[0, 0, 0, 0], [0, 1, 1, 1]], dig=[[0, 0], [0, 1], [1, 1]]
    )
    print(ans)
