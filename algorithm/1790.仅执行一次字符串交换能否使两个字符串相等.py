#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-23 17:13:17
LastEditTime: 2022-01-23 17:19:41
Description: 
FilePath: 1790.仅执行一次字符串交换能否使两个字符串相等.py
'''
#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start
from json.tool import main


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        elif sorted(s1) == sorted(s2):
            count = 0
            for letter1, letter2 in zip(s1, s2):
                if letter1 != letter2:
                    count += 1
            return count == 2
        else:
            return False
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.areAlmostEqual("bank", "kanb"))
