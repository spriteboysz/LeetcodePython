#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 16:52
LastEditTime: 2022-05-22 16:52
Description:
FilePath: 面试题 16.10. 生存人数.py.py
"""

from typing import List


class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        alive = [0 for _ in range(1900, 2001)]
        for b, d in zip(birth, death):
            for year in range(b - 1900, d - 1900 + 1):
                alive[year] += 1
        return alive.index(max(alive)) + 1900


if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxAliveYear(
        birth=[1900, 1901, 1950],
        death=[1948, 1951, 2000])
    print(ans)
