#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 13:21
FileName: algorithm
Description:P3090. 每个字符最多出现两次的最长子字符串.py
"""
from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maximum = left = 0
        count = Counter()
        for i, c in enumerate(s):
            count[c] += 1
            while count[c] > 2:
                count[s[left]] -= 1
                left += 1
            maximum = max(maximum, i - left + 1)
        return maximum


if __name__ == '__main__':
    print(Solution().maximumLengthSubstring("bcbbbcba"))
