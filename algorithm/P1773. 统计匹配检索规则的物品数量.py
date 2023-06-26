#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 17:44:20
LastEditTime: 2022-01-23 17:47:17
Description:
FilePath: 1773.统计匹配检索规则的物品数量.py
"""
#
# @lc app=leetcode.cn id=1773 lang=python3
#
# [1773] 统计匹配检索规则的物品数量
#

# @lc code=start
from typing import List 
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key = ["type", "color", "name"]
        count = 0
        for item in items:
            if item[key.index(ruleKey)] == ruleValue:
                count += 1
        return count
# @lc code=end

