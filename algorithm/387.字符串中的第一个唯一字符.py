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


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for v in sorted(list(set(s)), key=lambda el: s.index(el)):
            if s.count(v) == 1:
                return s.index(v)
        else:
            return -1
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("dddccdbba"))
