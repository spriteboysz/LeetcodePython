#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-09 22:59:47
LastEditTime: 2022-02-09 23:04:27
Description: 
FilePath: 2063.所有子字符串中的元音.py
'''
#
# @lc app=leetcode.cn id=2063 lang=python3
#
# [2063] 所有子字符串中的元音
#

# @lc code=start


class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        n = len(word)
        count = 0
        for i, item in enumerate(word):
            if item in vowels:
                count += (i + 1) * (n - i)
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.countVowels("aba"))
    print(s.countVowels("abc"))
    print(s.countVowels("ltcd"))
    print(s.countVowels("noosabasboosa"))
