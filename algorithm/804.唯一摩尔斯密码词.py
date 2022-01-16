#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-16 23:34:42
LastEditTime: 2022-01-16 23:41:13
Description: 
FilePath: 804.唯一摩尔斯密码词.py
'''
#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#

# @lc code=start
from typing import List
from string import ascii_lowercase


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        code = []
        for word in words:
            s = ""
            for letter in word:
                s += morse[ascii_lowercase.index(letter)]
            code.append(s)
        return len(set(code))
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
