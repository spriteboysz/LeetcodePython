#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-01 23:48:02
LastEditTime: 2022-02-01 23:55:35
Description:
FilePath: 1370.上升下降字符串.py
"""
#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def sortString(self, s: str) -> str:
        count = [0] * 26
        for item in s:
            count[ascii_lowercase.index(item)] += 1

        s2 = ""
        while len(s2) < len(s):
            for i in range(26):
                if count[i] > 0:
                    s2 += ascii_lowercase[i]
                    count[i] -= 1
            for i in range(25, -1, -1):
                if count[i] > 0:
                    s2 += ascii_lowercase[i]
                    count[i] -= 1
        return s2
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.sortString("aaaabbbbcccc"))
    print(s.sortString("rat"))
    print(s.sortString("leetcode"))
    print(s.sortString("ggggggg"))
    print(s.sortString("spo"))
