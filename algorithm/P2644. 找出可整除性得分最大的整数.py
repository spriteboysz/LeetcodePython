#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 22:22
FileName: algorithm/P2644. 找出可整除性得分最大的整数.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        dic = defaultdict(list)
        for divisor in divisors:
            dic[len([1 for num in nums if num % divisor == 0])].append(divisor)
        return min(dic[max(dic)])


if __name__ == '__main__':
    print(Solution().maxDivScore(nums=[4, 7, 9, 3, 9], divisors=[5, 2, 3]))
