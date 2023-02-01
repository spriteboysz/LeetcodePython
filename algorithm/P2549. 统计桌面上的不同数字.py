#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/31 22:57
FileName: algorithm/P2549. 统计桌面上的不同数字.py
Description: 
"""


class Solution:
    def distinctIntegers(self, n: int) -> int:
        return 1 if n == 1 else n - 1


if __name__ == '__main__':
    print(Solution().distinctIntegers(5))
