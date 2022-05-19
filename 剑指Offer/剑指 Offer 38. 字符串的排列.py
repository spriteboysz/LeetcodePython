#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-19 23:14:15
LastEditTime: 2022-05-19 23:19:56
Description: 
FilePath: 剑指 Offer 38. 字符串的排列.py
"""

from typing import List
from itertools import permutations


class Solution:
    def permutation(self, s: str) -> List[str]:
        permutation = set()
        for item in permutations(list(s)):
            permutation.add("".join(item))
        return list(permutation)


if __name__ == "__main__":
    solution = Solution()
    ans = solution.permutation(s="abc")
    print(ans)
