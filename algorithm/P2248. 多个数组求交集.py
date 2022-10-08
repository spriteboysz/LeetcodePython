#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 22:49
LastEditTime: 2022-05-27 22:49
Description:
FilePath: 2248.多个数组求交集.py
"""

from functools import reduce
from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(reduce(lambda a, b: set(a) & set(b), nums))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.intersection(
        nums=[[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]])
    print(ans)
