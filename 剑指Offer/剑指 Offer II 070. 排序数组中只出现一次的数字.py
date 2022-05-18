#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-18 22:58:37
LastEditTime: 2022-05-18 22:59:58
Description: 
FilePath: 剑指 Offer II 070. 排序数组中只出现一次的数字.py
"""

from typing import List
from functools import reduce


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)


if __name__ == "__main__":
    solution = Solution()
    ans = solution.singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8])
    print(ans)
    ans = solution.singleNonDuplicate(nums =  [3,3,7,7,10,11,11])
    print(ans)
