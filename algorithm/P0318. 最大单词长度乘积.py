#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-14 23:14:36
LastEditTime: 2022-02-14 23:22:54
Description: 
FilePath: 318.最大单词长度乘积.py
'''
#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                w1, w2 = set(words[i]), set(words[j])
                if len(w1 & w2) == 0:
                    maximum = max(maximum, len(words[i] * len(words[j])))
        return maximum
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
