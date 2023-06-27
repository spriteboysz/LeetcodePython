#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-01 22:49:52
LastEditTime: 2022-04-01 22:51:33
Description: 
FilePath: 74.搜索二维矩阵.py
"""
#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
from typing import List


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
    )
    print(ans)
    ans = solution.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    )
    print(ans)
