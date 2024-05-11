#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-08 22:26
FileName: algorithm
Description:P3034. 匹配模式数组的子数组数目 I.py 
"""
from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        patterns = []
        for i, num in enumerate(nums[1:], start=1):
            if nums[i] > nums[i - 1]:
                patterns.append(1)
            elif nums[i] < nums[i - 1]:
                patterns.append(-1)
            else:
                patterns.append(0)
        cnt, n = 0, len(pattern)
        for i in range(len(patterns) - n + 1):
            if patterns[i:i + n] == pattern:
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().countMatchingSubarrays(nums=[1, 4, 4, 1, 3, 5, 5, 3], pattern=[1, 0, -1]))
