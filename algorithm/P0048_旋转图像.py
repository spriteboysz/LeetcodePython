#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 15:33:28
LastEditTime: 2022-02-12 15:40:38
Description: 
FilePath: 48.旋转图像.py
'''
#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [list(row[::-1]) for row in zip(*matrix)]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
