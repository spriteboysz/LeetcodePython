#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-12 21:36:45
LastEditTime: 2022-03-12 21:38:37
Description: 
FilePath: 893.特殊等价字符串组.py
"""
#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#

# @lc code=start
from collections import defaultdict
from string import ascii_lowercase
from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        counts = defaultdict(list)
        for word in words:
            even, odd = [0] * 26, [0] * 26
            for letter in word[::2]:
                even[ascii_lowercase.index(letter)] += 1
            for letter in word[1::2]:
                odd[ascii_lowercase.index(letter)] += 1
            counts[(tuple(even), tuple(odd))].append(word)
        return len(counts)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numSpecialEquivGroups(
        words=["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
    )
    print(ans)
    ans = solution.numSpecialEquivGroups(
        words=["abc", "acb", "bac", "bca", "cab", "cba"]
    )
    print(ans)
