#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-15 17:23:36
LastEditTime: 2022-05-15 17:23:36
Description: 
FilePath: 剑指 Offer II 006. 排序数组中两个数字之和.py
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = {}
        for i, num in enumerate(numbers):
            if target - num in index:
                return [index[target - num], i]
            index[num] = i


if __name__ == "__main__":
    solution = Solution()
    ans = solution.twoSum([1, 2, 4, 6, 10], 8)
    print(ans)
