#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 00:28
FileName: LCP
Description:LCR 169. 招式拆解 II.py 
"""
from collections import defaultdict


class Solution:
    def dismantlingAction(self, arr: str) -> str:
        dic = defaultdict(int)
        for c in arr:
            dic[c] += 1
        for c in arr:
            if dic[c] == 1:
                return c
        return " "


if __name__ == '__main__':
    print(Solution().dismantlingAction(arr="abbccdeff"))
