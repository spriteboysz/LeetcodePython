#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 23:45
FileName: algorithm/P2437. 有效时间的数目.py
Description: 
"""


class Solution:
    def countTime(self, time: str) -> int:
        cnt = 0
        for i in range(24 * 60 - 1, -1, -1):
            hh, mm = divmod(i, 60)
            cur = "{:0>2d}:{:0>2d}".format(hh, mm)
            for j, el in enumerate(time):
                if el != "?" and el != cur[j]:
                    break
            else:
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().countTime("0?:0?"))
    print(Solution().countTime("??:??"))
