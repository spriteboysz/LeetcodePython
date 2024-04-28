#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-27 18:50
FileName: algorithm
Description:P2640. 一个数组所有前缀的分数.py 
"""
from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        score = []
        maximum, total = 0, 0
        for num in nums:
            maximum = max(maximum, num)
            total += num + maximum
            score.append(total)
        return score


if __name__ == '__main__':
    print(Solution().findPrefixScore(nums=[2, 3, 7, 5, 10]))
