#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-07 22:26:11
LastEditTime: 2022-01-10 23:40:45
Description: 
FilePath: 168.excel表列名称.py
'''
#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# @lc code=start
from string import ascii_uppercase


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = ""
        base = ascii_uppercase

        while columnNumber != 0:
            columnNumber -= 1
            columnNumber, mod = divmod(columnNumber, 26)
            column += base[mod]
        return column[::-1]


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(2147483647))
