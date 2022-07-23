#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-24 23:03:26
LastEditTime: 2022-02-24 23:07:32
Description: 
FilePath: 1780.判断一个数字是否可以表示成三的幂的和.py
"""
#
# @lc app=leetcode.cn id=1780 lang=python3
#
# [1780] 判断一个数字是否可以表示成三的幂的和
#

# @lc code=start
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n >= 2:
            n, mod = divmod(n, 3)
            if mod == 2:
                return False
        return True


# @lc code=end
