#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-25 22:50
LastEditTime: 2022-05-25 22:50
Description:
FilePath: 面试题 10.09. 排序矩阵查找.py
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        n, m = len(matrix), len(matrix[0])
        row, col = 0, m - 1
        while row != n and col != -1:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    ans = solution.searchMatrix([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5)
    print(ans)
