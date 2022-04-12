#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-12 23:18:43
LastEditTime: 2022-04-12 23:21:42
Description: 
FilePath: 2220.转换数字的最少位翻转次数.py
"""
#
# @lc app=leetcode.cn id=2220 lang=python3
#
# [2220] 转换数字的最少位翻转次数
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.minBitFlips(10, 7)
    print(ans)
    ans = solution.minBitFlips(3, 4)
    print(ans)
