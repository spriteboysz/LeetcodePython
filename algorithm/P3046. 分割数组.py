#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 17:14
FileName: algorithm
Description:P3046. 分割数组.py 
"""
from collections import defaultdict
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] > 2:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isPossibleToSplit(nums=[1, 1, 2, 2, 3, 4]))
