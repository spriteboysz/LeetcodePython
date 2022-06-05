#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 17:30
LastEditTime: 2022-06-05 17:30
Description:
FilePath: 剑指 Offer II 015. 字符串中的所有变位词.py
"""

from typing import List
from string import ascii_lowercase as lowercase


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr1, arr2 = [0] * 26, [0] * 26
        if len(s) < len(p):
            return []
        for i in range(len(p)):
            arr1[lowercase.index(s[i])] += 1
            arr2[lowercase.index(p[i])] += 1
        index = [0] if arr1 == arr2 else []
        for j in range(len(p), len(s)):
            arr1[lowercase.index(s[j])] += 1
            arr1[lowercase.index(s[j - len(p)])] -= 1
            if arr1 == arr2:
                index.append(j - len(p) + 1)
        return index


if __name__ == '__main__':
    solution = Solution()
    ans = solution.findAnagrams(s="cbaebabacd", p="abc")
    print(ans)
    ans = solution.findAnagrams(s="abab", p="ab")
    print(ans)
