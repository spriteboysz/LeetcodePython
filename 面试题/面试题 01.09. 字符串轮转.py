#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 23:06:10
LastEditTime: 2022-02-04 23:14:18
Description:
FilePath: 100162.字符串轮转.py
"""
#
# @lc app=leetcode.cn id=100162 lang=python3
#
# [面试题 01.09] 字符串轮转
#

# @lc code=start


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        elif len(s1) == len(s2) == 0:
            return True
        else:
            for i in range(0, len(s1)):
                if s1[i:] + s1[:i] == s2:
                    return True
            return False
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.isFlipedString("aa", "aba"))
    print(s.isFlipedString(s1="waterbottle", s2="erbottlewat"))
