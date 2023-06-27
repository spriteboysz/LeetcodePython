#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 14:26:10
LastEditTime: 2022-02-04 14:28:33
Description:
FilePath: 100280.替换空格.py
"""
#
# @lc app=leetcode.cn id=100280 lang=python3
#
# [剑指 Offer 05] 替换空格
#

# @lc code=start


class Solution:
    def replaceSpace(self, s: str) -> str:
        s2 = ""
        for item in s:
            s2 += "%20" if item == " " else item
            # if item == " ":
            #     s2 += "%20"
            # else:
            #     s2 += item
        return s2
# @lc code=end
