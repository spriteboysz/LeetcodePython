#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 11:07
FileName: algorithm/P2367. 算术三元组的数目.py
Description: 
"""
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n, cnt = len(nums), 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] != diff:
                    continue
                for k in range(j + 1, n):
                    if nums[k] - nums[j] == diff:
                        cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().arithmeticTriplets(nums=[4, 5, 6, 7, 8, 9], diff=2)
    print(solution)
