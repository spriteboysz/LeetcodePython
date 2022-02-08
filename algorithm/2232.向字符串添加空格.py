#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-08 22:27:58
LastEditTime: 2022-02-08 22:31:07
Description: 
FilePath: 2232.向字符串添加空格.py
'''
#
# @lc app=leetcode.cn id=2232 lang=python3
#
# [2109] 向字符串添加空格
#

# @lc code=start
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        for position in spaces[::-1]:
            s = s[:position] + " " + s[position:]
        return s
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.addSpaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15]))
    print(s.addSpaces(s="icodeinpython", spaces=[1, 5, 7, 9]))
    print(s.addSpaces(s="spacing", spaces=[0, 1, 2, 3, 4, 5, 6]))
