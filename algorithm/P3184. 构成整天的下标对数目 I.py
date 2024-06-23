#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-23 08:53
FileName: algorithm
Description:P3184. 构成整天的下标对数目 I.py 
"""
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = 0
        for i, num1 in enumerate(hours):
            for num2 in hours[i + 1:]:
                if (num1 + num2) % 24 == 0:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().countCompleteDayPairs(hours=[72, 48, 24, 3]))
