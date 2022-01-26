#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-26 23:41:41
LastEditTime: 2022-01-26 23:46:39
Description: 
FilePath: 1309.解码字母到整数映射.py
'''
#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26, 0, -1):
            num = str(i)
            if i >= 10:
                num += "#"
            s = s.replace(num, ascii_lowercase[i - 1])
        return s

# @lc code=end
