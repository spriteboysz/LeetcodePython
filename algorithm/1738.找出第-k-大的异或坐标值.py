#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 22:25:25
LastEditTime: 2022-04-09 22:29:34
Description: 
FilePath: 1738.找出第-k-大的异或坐标值.py
"""
#
# @lc app=leetcode.cn id=1738 lang=python3
#
# [1738] 找出第 K 大的异或坐标值
#

# @lc code=start
from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(1, m):
                matrix[i][j] ^= matrix[i][j - 1]

        for j in range(m):
            for i in range(1, n):
                matrix[i][j] ^= matrix[i - 1][j]

        values = []
        for i in range(n):
            values.extend(matrix[i])
        return sorted(values, reverse=True)[k - 1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.kthLargestValue(matrix=[[5, 2], [1, 6]], k=1)
    print(ans)
    ans = solution.kthLargestValue(matrix=[[5, 2], [1, 6]], k=2)
    print(ans)
    ans = solution.kthLargestValue(matrix=[[5, 2], [1, 6]], k=3)
    print(ans)
    ans = solution.kthLargestValue(matrix=[[5, 2], [1, 6]], k=4)
    print(ans)
