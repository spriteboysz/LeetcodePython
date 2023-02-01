#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/31 22:44
FileName: algorithm/P2451. 差值数组不同的字符串.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        dic = defaultdict(list)
        for word in words:
            keys = [ord(word[j + 1]) - ord(word[j]) for j in range(len(word) - 1)]
            dic[tuple(keys)].append(word)
        return next(v[0] for k, v in dic.items() if len(v) == 1)


if __name__ == '__main__':
    print(Solution().oddString(["adc", "wzy", "abc"]))
