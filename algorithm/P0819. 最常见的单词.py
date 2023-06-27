#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-09-28 23:13:48
Description:
FilePath: 819.最常见的单词.py
"""
#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for item in ["!", "?", "'", ",", ";", "."]:
            paragraph = paragraph.replace(item, " ")
        words = paragraph.lower().split()
        lst = list(set(words) - set(banned))
        count = list(map(lambda el: words.count(el), lst))
        return lst[count.index(max(count))]


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    m = s.mostCommonWord(
        "a, a, a, a, b,b,b,c, c", ["a"])
    print(m)
