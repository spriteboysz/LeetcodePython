#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-29 23:57:15
LastEditTime: 2022-01-30 00:10:23
Description: 
FilePath: 2027.转换字符串的最少操作次数.py
'''
#
# @lc app=leetcode.cn id=2027 lang=python3
#
# [2027] 转换字符串的最少操作次数
#

# @lc code=start


class Solution:
    def minimumMoves(self, s: str) -> int:
        count1, count2 = 0, 0
        for i in range(0, len(s), 3):
            if "X" in s[i:i + 3]:
                count1 += 1
        for i in range(len(s) - 1, -1, -3):
            if "X" in s[max(0, i-2):i+1]:
                count2 += 1
        return min(count1, count2)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    # print(s.minimumMoves("XXX"))
    print(s.minimumMoves("XXOX"))
    # print(s.minimumMoves("XX0X"))
