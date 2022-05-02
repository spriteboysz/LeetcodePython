#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 14:19:35
LastEditTime: 2022-02-04 14:20:01
Description: 
FilePath: 100292.二进制中-1-的个数.py
'''
#
# @lc app=leetcode.cn id=100292 lang=python3
#
# [剑指 Offer 15] 二进制中1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
        
# @lc code=end

