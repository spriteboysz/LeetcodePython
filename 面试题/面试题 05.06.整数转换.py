#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 15:35:32
LastEditTime: 2022-02-04 15:47:21
Description: 
FilePath: 100181.整数转换.py
"""
#
# @lc app=leetcode.cn id=100181 lang=python3
#
# [面试题 05.06] 整数转换
#

# @lc code=start


class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        return bin((A & 0xFFFFFFFF) ^ (B & 0xFFFFFFFF)).count("1")


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(bin(826966453))
    print(bin(-729934991))
    print(s.convertInteger(826966453, -729934991))
