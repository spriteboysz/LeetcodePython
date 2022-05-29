#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 22:07
LastEditTime: 2022-05-29 22:07
Description:
FilePath: 面试题29. 顺时针打印矩阵.py
"""


class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix:
            return []

        left, right, top, bottom, nums = 0, len(
            matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(left, right + 1):
                nums.append(matrix[top][i])  # left to right
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom + 1):
                nums.append(matrix[i][right])  # top to bottom
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                nums.append(matrix[bottom][i])  # right to left
            bottom -= 1
            if top > bottom:
                break
            for i in range(bottom, top - 1, -1):
                nums.append(matrix[i][left])  # bottom to top
            left += 1
            if left > right:
                break
        return nums


if __name__ == '__main__':
    solution = Solution()
    ans = solution.spiralOrder(
        matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(ans)
