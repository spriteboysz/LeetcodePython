#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-22 21:52:37
LastEditTime: 2022-01-22 22:03:45
Description: 
FilePath: 2022.将一维数组转变成二维数组.py
'''
#
# @lc app=leetcode.cn id=2022 lang=python3
#
# [2022] 将一维数组转变成二维数组
#

# @lc code=start
from copyreg import constructor
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) == m * n:
            matrix = [[0] * n for _ in range(m)]
            j = 0
            for i in range(m):
                matrix[i] = original[j:j + n]
                j += n
            return matrix
        else:
            return []

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.construct2DArray(original=[1, 2, 3], m=1, n=3))
    print(s.construct2DArray(original=[1, 2], m=1, n=1))
    print(s.construct2DArray(original=[3], m=1, n=2))
