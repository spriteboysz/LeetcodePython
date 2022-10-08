#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 16:06:13
LastEditTime: 2022-02-04 21:43:14
Description: 
FilePath: 2254.检查是否每一行每一列都包含全部整数.py
'''
#
# @lc app=leetcode.cn id=2254 lang=python3
#
# [2133] 检查是否每一行每一列都包含全部整数
#

# @lc code=start
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        target = [i for i in range(1, n + 1)]
        for row in matrix:
            if sorted(row) != target:
                return False
        for row in zip(*matrix):
            if sorted(list(row)) != target:
                return False
        return True
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.checkValid([[1, 1, 1], [1, 2, 3], [1, 2, 3]]))
