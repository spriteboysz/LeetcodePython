#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-27 22:56:30
LastEditTime: 2022-01-27 23:05:01
Description: 
FilePath: 1582.二进制矩阵中的特殊位置.py
'''
#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#

# @lc code=start
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        column = []
        for c in zip(*mat):
            column.append(sum(c))

        count = 0
        for row in mat:
            if sum(row) == 1:
                for j in range(len(row)):
                    if row[j] == 1 and column[j] == 1:
                        count += 1
        return count


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.numSpecial([[0, 0, 0, 1],
                        [1, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0]]))
