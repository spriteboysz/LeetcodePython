#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 23:33:21
LastEditTime: 2022-01-22 23:38:03
Description:
FilePath: 1941.检查是否所有字符出现次数相同.py
"""
#
# @lc app=leetcode.cn id=1941 lang=python3
#
# [1941] 检查是否所有字符出现次数相同
#

# @lc code=start


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(map(lambda el: s.count(el), set(s)))) == 1

# @lc code=end
