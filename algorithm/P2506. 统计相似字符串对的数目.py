#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/28 23:26
FileName: algorithm/P2506. 统计相似字符串对的数目.py
Description: 
"""
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        for i, word in enumerate(words):
            words[i] = "".join(sorted(set(list(word))))

        cnt = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j]:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))
    print(Solution().similarPairs(["aabb", "ab", "ba"]))
