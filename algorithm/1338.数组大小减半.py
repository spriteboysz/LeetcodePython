#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-03 22:30:53
LastEditTime: 2022-04-03 22:37:39
Description: 
FilePath: 1338.数组大小减半.py
"""
#
# @lc app=leetcode.cn id=1338 lang=python3
#
# [1338] 数组大小减半
#

# @lc code=start

from typing import List
from collections import defaultdict


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        numcount = defaultdict(int)
        for num in arr:
            numcount[num] += 1
        count = sorted(numcount.values(), reverse=True)
        # print(count)
        minimum, length = 0, len(arr)
        for i, c in enumerate(count):
            minimum += c
            if minimum >= length / 2:
                return i + 1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7])
    print(ans)
    ans = solution.minSetSize([7, 7, 7, 7, 7, 7])
    print(ans)
    ans = solution.minSetSize([1])
    print(ans)
    ans = solution.minSetSize([1000, 1000, 3, 7])
    print(ans)
    ans = solution.minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(ans)
