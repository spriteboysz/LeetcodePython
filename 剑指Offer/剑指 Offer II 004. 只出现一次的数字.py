#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-15 17:01:20
LastEditTime: 2022-05-15 17:04:03
Description: 
FilePath: 剑指 Offer II 004. 只出现一次的数字.py
"""
from typing import List
from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        for n, c in count.items():
            if c == 1:
                return n


if __name__ == "__main__":
    solution = Solution()
    ans = solution.singleNumber([2, 2, 3, 2])
    print(ans)
