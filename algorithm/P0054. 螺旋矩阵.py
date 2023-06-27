#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-16 23:51:27
LastEditTime: 2022-04-16 23:57:59
Description: 
FilePath: 54.螺旋矩阵.py
"""
#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        direction, order = [(0, 1), (1, 0), (0, -1), (-1, 0)], []
        x, y = 0, 0
        dx, dy = direction.pop(0)
        direction.append((dx, dy))
        while len(order) < m * n:
            order.append(matrix[x][y])
            matrix[x][y] = "inf"
            if (
                    0 <= x + dx <= m - 1
                    and 0 <= y + dy <= n - 1
                    and matrix[x + dx][y + dy] != "inf"
            ):
                pass
            else:
                dx, dy = direction.pop(0)
                direction.append((dx, dy))
            x, y = x + dx, y + dy
        return order


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(ans)
