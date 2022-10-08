#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-20 22:48:46
LastEditTime: 2022-01-20 23:05:28
Description: 
FilePath: 1002.查找共用字符.py
'''
#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

from functools import reduce
# @lc code=start
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = list(reduce(lambda x, y: set(x) & set(y), words))
        count = [101] * len(common)
        for word in words:
            for i, letter in enumerate(common):
                count[i] = min(count[i], word.count(letter))

        commonChars = []
        for letter, c in zip(common, count):
            commonChars.extend([letter] * c)
        return commonChars


# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(["cool", "lock", "cook"]))
    print(s.commonChars(["bella", "label", "roller"]))
