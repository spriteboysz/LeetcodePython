#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-28 23:13:11
LastEditTime: 2022-01-28 23:20:11
Description: 
FilePath: 720.词典中最长的单词.py
'''
#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key=lambda el: (-len(el), el))
        for word in words:
            for i in range(len(word) - 1):
                if word[:-i-1] not in words:
                    break
            else:
                return word
        return ""
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.longestWord(["w", "wo", "wor", "worl", "world"]))
