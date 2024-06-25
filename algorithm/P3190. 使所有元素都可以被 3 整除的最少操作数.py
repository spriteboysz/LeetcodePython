#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-25 23:13
FileName: algorithm
Description:P3190. 使所有元素都可以被 3 整除的最少操作数.py 
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if num % 3 != 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().minimumOperations(nums=[1, 2, 3, 4]))
