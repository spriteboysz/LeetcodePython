#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-23 17:01:05
LastEditTime: 2022-01-23 17:09:47
Description: 
FilePath: 1796.字符串中第二大的数字.py
'''
#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#

# @lc code=start


class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()
        for item in s:
            if item.isdigit():
                nums.add(item)
        if len(nums) <= 1:
            return -1
        else:
            nums.remove(max(nums))
            return int(max(nums))

# @lc code=end
