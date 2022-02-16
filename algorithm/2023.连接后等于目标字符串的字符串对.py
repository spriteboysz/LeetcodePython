#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 22:23:13
LastEditTime: 2022-02-16 22:26:44
Description: 
FilePath: 2023.连接后等于目标字符串的字符串对.py
"""
#
# @lc app=leetcode.cn id=2023 lang=python3
#
# [2023] 连接后等于目标字符串的字符串对
#

# @lc code=start
from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    count += 1
        return count


# @lc code=end
