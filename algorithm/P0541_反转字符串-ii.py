#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-13 22:46:02
LastEditTime: 2022-01-13 22:59:07
Description: 
FilePath: 541.反转字符串-ii.py
'''
#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s2 = ""
        for i, j in zip(range(0, len(s), k), range(10000)):
            if j % 2 == 0:
                s2 += s[i:i+k][::-1]
            else:
                s2 += s[i:i+k]
        return s2
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefgh", 3))
