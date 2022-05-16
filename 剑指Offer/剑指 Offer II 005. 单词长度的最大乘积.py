#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-15 17:08:17
LastEditTime: 2022-05-15 17:08:18
Description: 
FilePath: 剑指 Offer II 005. 单词长度的最大乘积.py
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(set(words[i] + words[j])) == len(set(words[i])) + len(set(words[j])):
                    maximum = max(maximum, len(words[i] * len(words[j])))
        return maximum


if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxProduct(words=["abcw", "baz", "foo", "bar", "fxyz", "abcdef"])
    print(ans)
    ans = solution.maxProduct(
        ["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]
    )
    print(ans)
