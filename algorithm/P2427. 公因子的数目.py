#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 22:54
FileName: algorithm/P2427. 公因子的数目.py
Description: 
"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        cnt = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().commonFactors(25, 30)
    print(solution)
    solution = Solution().commonFactors(12, 6)
    print(solution)
