#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-27 23:07:07
LastEditTime: 2022-01-27 23:12:49
Description:
FilePath: 1572.矩阵对角线元素的和.py
"""
#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

# @lc code=start
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            count += mat[i][i] + mat[i][-i - 1]
        if len(mat) % 2 == 1:
            count -= mat[len(mat) // 2][len(mat) // 2]
        return count


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.diagonalSum([[5]]))
