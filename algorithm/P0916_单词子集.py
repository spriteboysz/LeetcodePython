#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-15 21:24:47
LastEditTime: 2022-03-15 21:40:24
Description: 
FilePath: 916.单词子集.py
"""
#
# @lc app=leetcode.cn id=916 lang=python3
#
# [916] 单词子集
#

from string import ascii_lowercase
# @lc code=start
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        lettercount = [0] * 26
        for word in words2:
            temp = [0] * 26
            for letter in word:
                temp[ascii_lowercase.index(letter)] += 1
            for i in range(26):
                lettercount[i] = max(lettercount[i], temp[i])

        common = []
        for word in words1:
            letter = [0] * 26
            for item in word:
                letter[ascii_lowercase.index(item)] += 1
            for cur, target in zip(letter, lettercount):
                if cur < target:
                    break
            else:
                common.append(word)
        return common


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.wordSubsets(
        ["amazon", "apple", "facebook", "google", "leetcode"], words2=["e", "o"]
    )
    print(ans)
    ans = solution.wordSubsets(
        words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["l", "e"]
    )
    print(ans)
    ans = solution.wordSubsets(
        words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["e", "oo"]
    )
    print(ans)
    ans = solution.wordSubsets(
        words1=["amazon", "apple", "facebook", "google", "leetcode"],
        words2=["lo", "eo"],
    )
    print(ans)
    ans = solution.wordSubsets(
        words1=["amazon", "apple", "facebook", "google", "leetcode"],
        words2=["ec", "oc", "ceo"],
    )
    print(ans)
