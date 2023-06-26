#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-21 23:24:12
LastEditTime: 2022-01-21 23:27:27
Description:
FilePath: 2068.检查两个字符串是否几乎相等.py
"""
#
# @lc app=leetcode.cn id=2068 lang=python3
#
# [2068] 检查两个字符串是否几乎相等
#

# @lc code=start


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        letters = list(set(word1) | set(word2))
        for letter in letters:
            if abs(word1.count(letter) - word2.count(letter)) > 3:
                return False
        return True
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.checkAlmostEquivalent(word1="cccddabba", word2="babababab"))
    print(s.checkAlmostEquivalent(word1="abcdeef", word2="abaaacc"))
