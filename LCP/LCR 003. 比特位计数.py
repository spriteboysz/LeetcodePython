#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 20:23
FileName: LCP
Description:LCR 003. 比特位计数.py 
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        for i in range(n + 1):
            cur, cnt = i, 0
            while cur:
                cur &= cur - 1
                cnt += 1
            bits.append(cnt)
        return bits


if __name__ == '__main__':
    print(Solution().countBits(5))
