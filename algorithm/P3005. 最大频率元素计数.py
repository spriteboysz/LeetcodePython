#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 13:30
FileName: algorithm
Description:P3005. 最大频率元素计数.py 
"""
from typing import List
from collections import defaultdict


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        maximum = max(count.values())
        return sum([cnt for cnt in count.values() if cnt == maximum])


if __name__ == '__main__':
    print(Solution().maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4]))
