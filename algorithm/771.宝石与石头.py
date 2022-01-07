#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-05 21:46:42
Description: 宝石与石头
FilePath: 771.宝石与石头.py
'''
#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for item in jewels:
            count += stones.count(item)

        return count
# @lc code=end

