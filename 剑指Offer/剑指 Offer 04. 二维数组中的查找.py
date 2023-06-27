#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-26 22:47
LastEditTime: 2022-05-26 22:47
Description:
FilePath: 剑指 Offer 04. 二维数组中的查找.py
"""

from typing import List


class Solution:
    def findNumberIn2DArray(self,
                            matrix: List[List[int]],
                            target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    ans = solution.findNumberIn2DArray([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5)
    print(ans)
