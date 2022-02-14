#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-14 23:29:59
LastEditTime: 2022-02-14 23:36:38
Description: 
FilePath: 119.杨辉三角-ii.py
'''
#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        for _ in range(2, rowIndex + 2):
            row = []
            for j in range(1, len(triangle[-1])):
                row += [triangle[-1][j - 1] + triangle[-1][j]]
            triangle.append([1] + row + [1])
        return triangle[-1]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.getRow(6))