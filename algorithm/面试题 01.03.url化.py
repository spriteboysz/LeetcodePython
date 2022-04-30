#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 15:51:02
LastEditTime: 2022-02-04 15:57:52
Description: 
FilePath: 100160.url化.py
'''
#
# @lc app=leetcode.cn id=100160 lang=python3
#
# [面试题 01.03] URL化
#

# @lc code=start


class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        url = ""
        if len(S.strip()) < length:
            url += "%20" * (length - len(S.strip()))
        for item in S.strip():
            if item == " ":
                url += "%20"
            else:
                url += item
        return url
# @lc code=end
