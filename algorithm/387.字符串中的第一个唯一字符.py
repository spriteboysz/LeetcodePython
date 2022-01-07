#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-27 23:02:12
Description: 
FilePath: 387.字符串中的第一个唯一字符.py
'''
#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        t = Counter.values(s)
        print(t)
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.firstUniqChar("leetcode")
    