#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-11 23:42:07
LastEditTime: 2022-01-11 23:51:58
Description:
FilePath: 336.回文对.py
"""
#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#

# @lc code=start
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                word = word1 + word2
                if word1 != word2 and word == word[::-1]:
                    pairs.append([i, j])
        return pairs


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.palindromePairs(["bat", "tab", "cat"]))
    print(s.palindromePairs(["a", ""]))
