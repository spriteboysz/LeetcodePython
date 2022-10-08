#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-29 23:57:15
LastEditTime: 2022-02-18 22:09:33
Description: 
FilePath: 2027.转换字符串的最少操作次数.py
"""
#
# @lc app=leetcode.cn id=2027 lang=python3
#
# [2027] 转换字符串的最少操作次数
#

# @lc code=start


class Solution:
    def minimumMoves(self, s: str) -> int:
        count, i = 0, 0
        while i < len(s):
            if s[i] == "X":
                count += 1
                i += 3
            else:
                i += 1
        return count


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minimumMoves("XXX"))
    print(s.minimumMoves("XXOX"))
    print(s.minimumMoves("XX0X"))
