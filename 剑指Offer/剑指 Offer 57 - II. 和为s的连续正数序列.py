#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-20 23:17:43
LastEditTime: 2022-05-20 23:20:11
Description: 
FilePath: 剑指 Offer 57 - II. 和为s的连续正数序列.py
"""

from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, res = 1, 2, []
        while i < j:
            j = (-1 + (1 + 4 * (2 * target + i * i - i)) ** 0.5) / 2
            if i < j and j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    ans = solution.findContinuousSequence(15)
    print(ans)
    ans = solution.findContinuousSequence(9)
    print(ans)
