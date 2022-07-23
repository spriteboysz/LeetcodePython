#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-10 23:45:30
LastEditTime: 2022-01-10 23:51:14
Description: 
FilePath: 171.excel-表列序号.py
'''
#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
from string import ascii_uppercase


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = ascii_uppercase
        num = 0
        for i, v in enumerate(list(columnTitle)):
            num += (base.index(v) + 1) * 26 ** (len(columnTitle) - 1 - i)
        return num

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber("FXSHRXW"))
