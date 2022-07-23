#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-23 17:48:58
LastEditTime: 2022-01-23 18:00:19
Description: 
FilePath: 1768.交替合并字符串.py
'''
#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#

# @lc code=start


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        for letter1, letter2 in zip(word1, word2):
            word += letter1 + letter2
        if len(word1) > len(word2):
            return word + word1[len(word2):]
        elif len(word1) < len(word2):
            return word + word2[len(word1):]
        else:
            return word
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("cdf", "a"))
    print(s.mergeAlternately("abce", "pq"))
