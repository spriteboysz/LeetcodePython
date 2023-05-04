#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-04 22:59
FileName: algorithm/P2578. 最小和分割.py
Description: 
"""


class Solution:
    def splitNum(self, num: int) -> int:
        ss = sorted(list(str(num)))
        return int("".join(ss[::2])) + int("".join(ss[1::2]))


if __name__ == '__main__':
    print(Solution().splitNum(4325))
