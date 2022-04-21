#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 22:52:57
LastEditTime: 2022-04-21 22:54:18
Description: 
FilePath: 1668.最大重复子字符串.py
"""
#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for i in range(len(sequence) // len(word), -1, -1):
            if word * i in sequence:
                return i


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
    ans = s.maxRepeating(sequence = "ababc", word = "ab")
    print(ans)
    ans = s.maxRepeating(sequence = "ababc", word = "ac")
    print(ans)