#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/31 22:59
FileName: algorithm/P2389. 和有限的最长子序列.py
Description: 
"""
from typing import List
from math import inf


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        nums += [inf]

        res = []
        for query in queries:
            for i, num in enumerate(nums):
                if num > query:
                    res.append(i)
                    break
        return res


if __name__ == '__main__':
    print(Solution().answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21]))
