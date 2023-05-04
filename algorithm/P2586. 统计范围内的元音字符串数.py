#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-04 22:51
FileName: algorithm/P2586. 统计范围内的元音字符串数.py
Description: 
"""
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        cnt = 0
        vowels = "aeiouAEIOU"
        for i in range(left, right + 1):
            if vowels.find(words[i][0]) >= 0 and vowels.find(words[i][-1]) >= 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().vowelStrings(words=["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4))
