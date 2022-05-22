#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-21 23:27:04
LastEditTime: 2022-05-21 23:28:41
Description: 
FilePath: 剑指 Offer II 083. 没有重复元素集合的全排列.py
"""

from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, permutations(nums)))


if __name__ == "__main__":
    solution = Solution()
    ans = solution.permute([1, 2, 3])
    print(ans)
