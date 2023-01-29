#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/29 21:59
FileName: algorithm/P2515. 到目标字符串的最短距离.py
Description: 
"""
from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = n = len(words)
        for i, word in enumerate(words):
            if word == target:
                ans = min(ans, abs(i - startIndex), n - abs(i - startIndex))
        return ans if ans < n else -1


if __name__ == '__main__':
    print(Solution().closetTarget(words=["hello", "i", "am", "leetcode", "hello"], target="hello", startIndex=1))
