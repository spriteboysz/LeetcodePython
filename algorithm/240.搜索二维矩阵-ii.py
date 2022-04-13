#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 23:10:31
LastEditTime: 2022-04-13 23:13:27
Description: 
FilePath: 240.搜索二维矩阵-ii.py
"""
#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j <= len(matrix[0]) - 1:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.searchMatrix(
        matrix=[
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        target=5,
    )
    print(ans)
    ans = solution.searchMatrix(
        matrix=[
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        target=20,
    )
    print(ans)
