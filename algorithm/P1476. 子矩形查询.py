#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-15 22:33:23
LastEditTime: 2022-02-15 22:41:50
Description: 
FilePath: 1476.子矩形查询.py
'''
#
# @lc app=leetcode.cn id=1476 lang=python3
#
# [1476] 子矩形查询
#

# @lc code=start
from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2 + 1):
            self.rectangle[r][col1:col2 + 1] = [newValue] * (col2+1-col1)
            # for c in range(col1, col2 + 1):
            #     self.rectangle[r][c] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
# @lc code=end
