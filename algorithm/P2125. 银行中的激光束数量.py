#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-11 23:07
FileName: algorithm/P2125. 银行中的激光束数量.py
Description: 
"""
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = []
        for row in bank:
            cur = sum(map(int, row))
            if cur != 0:
                lasers.append(cur)
        count = 0
        for i in range(len(lasers) - 1):
            count += lasers[i] * lasers[i + 1]
        return count


if __name__ == '__main__':
    print(Solution().numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
