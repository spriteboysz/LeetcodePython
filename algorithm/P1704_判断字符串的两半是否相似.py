#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-23 22:20:01
LastEditTime: 2022-01-23 22:26:27
Description: 
FilePath: 1704.判断字符串的两半是否相似.py
'''
#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#

# @lc code=start


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        a, b = s[:len(s)//2], s[len(s)//2:]
        count1, count2 = 0, 0
        for item1, item2 in zip(a, b):
            if item1 in vowel:
                count1 += 1
            if item2 in vowel:
                count2 += 1
        return count1 == count2
# @lc code=end
