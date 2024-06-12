#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-03 22:00
FileName: algorithm
Description:P3168. 候诊室中的最少椅子数.py 
"""


class Solution:
    def minimumChairs(self, s: str) -> int:
        maximum, cur = 0, 0
        for ch in s:
            if ch == 'E':
                cur += 1
            else:
                cur -= 1
            maximum = max(maximum, cur)
        return maximum


if __name__ == '__main__':
    print(Solution().minimumChairs(s="ELELEEL"))
