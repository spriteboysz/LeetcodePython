#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-24 23:25
FileName: algorithm/P2357. 使数组中所有元素都等于零.py
Description: 
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set([num for num in nums if num != 0]))


if __name__ == '__main__':
    solution = Solution().minimumOperations([1, 5, 0, 3, 5])
    print(solution)
