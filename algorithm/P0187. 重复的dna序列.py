#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-11 23:58:52
LastEditTime: 2022-02-12 00:02:27
Description:
FilePath: 187.重复的dna序列.py
"""
#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

from collections import defaultdict
# @lc code=start
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counts = defaultdict(int)
        for i in range(len(s) - 9):
            counts[s[i:i + 10]] += 1
        return [key for key, value in counts.items() if value >= 2]


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
