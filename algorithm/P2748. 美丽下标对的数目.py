#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-08 22:20
FileName: algorithm/P2748. 美丽下标对的数目.py
Description: 
"""
from math import gcd
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        cnt, n = 0, len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                a = int(str(nums[i])[0])
                b = int(str(nums[j])[-1])
                if gcd(a, b) == 1:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().countBeautifulPairs(nums=[2, 5, 1, 4]))
