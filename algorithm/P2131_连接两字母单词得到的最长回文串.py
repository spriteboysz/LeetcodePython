#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-20 15:44:01
LastEditTime: 2022-03-20 16:05:20
Description: 
FilePath: 2131.连接两字母单词得到的最长回文串.py
"""
#
# @lc app=leetcode.cn id=2131 lang=python3
#
# [2131] 连接两字母单词得到的最长回文串
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordcount, count, center = Counter(words), 0, 0
        print(wordcount)

        for word in wordcount:
            if word[0] == word[1]:
                if wordcount[word] % 2:
                    center = 1
                count += 4 * (wordcount[word] // 2)
            elif (reverse := word[::-1]) in wordcount:
                cur = min(wordcount[word], wordcount[reverse])
                count += 4 * cur
                wordcount[word] -= cur
                wordcount[reverse] -= cur
        return count + 2 * center


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.longestPalindrome(["lc", "cl", "gg", "mm", "mm"])
    print(ans)
