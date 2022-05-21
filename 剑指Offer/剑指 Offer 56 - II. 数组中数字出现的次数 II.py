#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-20 23:09:52
LastEditTime: 2022-05-20 23:09:54
Description: 
FilePath: 剑指 Offer 56 - II. 数组中数字出现的次数 II.py
"""

from typing import List
from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for num, c in count.items():
            if c == 1:
                return num


if __name__ == "__main__":
    solution = Solution()
    ans = solution.singleNumber(nums=[9, 1, 7, 9, 7, 9, 7])
    print(ans)
