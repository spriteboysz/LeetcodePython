#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-23 16:23:55
LastEditTime: 2022-01-23 16:26:15
Description: 
FilePath: 1876.长度为三且各字符不同的子字符串.py
'''
#
# @lc app=leetcode.cn id=1876 lang=python3
#
# [1876] 长度为三且各字符不同的子字符串
#

# @lc code=start
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            if s[i] != s[i + 1] != s[i + 2] != s[i]:
                count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.countGoodSubstrings("aababcabc"))
