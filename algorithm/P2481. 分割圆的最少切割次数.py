#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/29 22:03
FileName: algorithm/P2481. 分割圆的最少切割次数.py
Description: 
"""


class Solution:
    def numberOfCuts(self, n: int) -> int:
        return n if n > 1 and n % 2 else n // 2


if __name__ == '__main__':
    print(Solution().numberOfCuts(4))
    print(Solution().numberOfCuts(3))
