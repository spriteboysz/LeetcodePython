#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-01 19:55:09
Description: 杨辉三角
FilePath: 118.杨辉三角.py
'''
#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        if numRows == 1:
            row = [1]
        pass
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.generate(3))
