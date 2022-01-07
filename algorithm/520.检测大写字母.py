#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-29 00:19:42
Description: 检测大写字母
FilePath: 520.检测大写字母.py
'''
#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lst = []
        for c in word:
            if c.isupper():
                lst.append("u")
            elif c.islower():
                lst.append("l")

        if len(list(set(lst))) == 1:
            return True
        elif lst[0] == "u" and lst.count("l") == len(lst) - 1:
            return True
        return False
    
# @lc code=end

