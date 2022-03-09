#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-09 22:07:28
LastEditTime: 2022-03-09 22:09:25
Description: 
FilePath: 890.查找和替换模式.py
"""
#
# @lc app=leetcode.cn id=890 lang=python3
#
# [890] 查找和替换模式
#

# @lc code=start
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matching = []
        for word in filter(lambda el: len(el) == len(pattern), words):
            for i in range(len(word)):
                if word.index(word[i]) != pattern.index(pattern[i]):
                    break
            else:
                matching.append(word)
        return matching


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    ans = solution.findAndReplacePattern(
        words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"
    )
    print(ans)
