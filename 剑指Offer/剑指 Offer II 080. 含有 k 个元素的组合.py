#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 10:36
LastEditTime: 2022-05-22 10:36
Description:
FilePath: 剑指 Offer II 080. 含有 k 个元素的组合.py.py
"""

from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, combinations(range(1, n + 1), k)))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.combine(n=4, k=2)
    print(ans)
