#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 16:14:21
LastEditTime: 2022-01-23 16:21:58
Description:
FilePath: 1880.检查某单词是否等于两单词之和.py
"""
#
# @lc app=leetcode.cn id=1880 lang=python3
#
# [1880] 检查某单词是否等于两单词之和
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def transformation(self, word: str) -> int:
        num = ""
        for letter in word:
            num += str(ascii_lowercase.index(letter))
        return int(num)

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.transformation(firstWord) + self.transformation(secondWord) == self.transformation(targetWord)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.isSumEqual("aaa", "a", "aaaa"))
