#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-08 22:15
FileName: algorithm/P2744. 最大字符串配对数目.py
Description: 
"""
from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt, visited = 0, set()
        for word in words:
            if word[::-1] in visited:
                cnt += 1
            else:
                visited.add(word)
        return cnt


if __name__ == '__main__':
    print(Solution().maximumNumberOfStringPairs(words=["cd", "ac", "dc", "ca", "zz"]))
