#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-17 23:55:00
LastEditTime: 2022-01-18 00:00:50
Description:
FilePath: 867.转置矩阵.py
"""
#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
from typing import List 

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))
    
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.transpose([[1,2,3],[4,5,6]]))
    

