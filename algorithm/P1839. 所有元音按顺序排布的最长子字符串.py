#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-09 22:34:48
LastEditTime: 2022-02-09 22:41:19
Description:
FilePath: 1839.所有元音按顺序排布的最长子字符串.py
"""
#
# @lc app=leetcode.cn id=1839 lang=python3
#
# [1839] 所有元音按顺序排布的最长子字符串
#

# @lc code=start
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        count = [1] * len(word)
        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                count[i] = count[i - 1] + 1
                count[i - 1] = 0
        zipcount, zipword = [], []
        for i, item in enumerate(count):
            if item != 0:
                zipcount.append(item)
                zipword.append(word[i])
        maximum = 0
        for i in range(len(zipword) - 4):
            if zipword[i:i+5] == ["a", "e", "i", "o", "u"]:
                maximum = max(maximum, sum(zipcount[i:i+5]))
        return maximum
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.longestBeautifulSubstring("aeeeiiiioooauuuaeiou"))
    print(s.longestBeautifulSubstring("a"))
