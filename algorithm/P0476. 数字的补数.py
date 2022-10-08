#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-28 23:58:51
LastEditTime: 2022-01-28 23:59:33
Description: 
FilePath: 476.数字的补数.py
'''
#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        else:
            binary = bin(num).replace("0b", "").lstrip("0")
            return 2 ** (len(binary)) - 1 - num
# @lc code=end

