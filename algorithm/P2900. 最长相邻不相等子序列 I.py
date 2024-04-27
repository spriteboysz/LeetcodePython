#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-27 13:20
FileName: algorithm
Description:P2900. 最长相邻不相等子序列 I.py 
"""
from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        for i in range(1, len(groups)):
            if groups[i - 1] == groups[i]:
                groups[i - 1] = -1
        sequence = []
        for word, group in zip(words, groups):
            if group >= 0:
                sequence.append(word)
        return sequence


if __name__ == '__main__':
    print(Solution().getLongestSubsequence(words=["e", "a", "b"], groups=[0, 0, 1]))
