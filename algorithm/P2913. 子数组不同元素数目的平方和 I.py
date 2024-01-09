#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-08 22:32
FileName: algorithm
Description:P2913. 子数组不同元素数目的平方和 I.py 
"""
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums) + 1):
            for j in range(i + 1, len(nums) + 1):
                cnt = (cnt + len(set(nums[i: j])) ** 2) % 1000000007
        return cnt


if __name__ == '__main__':
    print(Solution().sumCounts([1, 2, 3]))
