#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 23:39
FileName: LCP
Description:LCR 190. 加密运算.py 
"""


class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        return sum([dataA, dataB])


if __name__ == '__main__':
    print(Solution().encryptionCalculate(dataA=5, dataB=-1))
