#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-28 22:17
LastEditTime: 2022-05-28 22:17
Description:
FilePath: 458.可怜的小猪.py
"""

from math import log, ceil


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets, minutesToTest // minutesToDie + 1))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.poorPigs(buckets=1000, minutesToDie=15, minutesToTest=60)
    print(ans)
