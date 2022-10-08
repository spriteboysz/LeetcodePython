#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-17 23:30:18
LastEditTime: 2022-01-17 23:34:25
Description: 
FilePath: 844.比较含退格的字符串.py
'''
#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, t1 = "", ""
        for item in s:
            if item == "#":
                s1 = s1[:-1]
            else:
                s1 += item
        for item in t:
            if item == "#":
                t1 = t1[:-1]
            else:
                t1 += item
        return s1 == t1

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare("ab##", "c#d#"))
    print(s.backspaceCompare("a#c", "b"))
