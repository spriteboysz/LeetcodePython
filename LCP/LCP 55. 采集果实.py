#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 23:14
LastEditTime: 2022-05-27 23:14
Description:
FilePath: LCP 55. 采集果实.py
"""

from typing import List
from math import ceil


class Solution:
    def getMinimumTime(self,
                       time: List[int],
                       fruits: List[List[int]],
                       limit: int) -> int:
        return sum([ceil(num / limit) * time[type] for type, num in fruits])
        # times = 0
        # for type, num in fruits:
        #     times += ceil(num / limit) * time[type]
        # return times


if __name__ == '__main__':
    solution = Solution()
    ans = solution.getMinimumTime(time=[2, 3, 2], fruits=[
        [0, 2], [1, 4], [2, 1]], limit=3)
    print(ans)
    ans = solution.getMinimumTime(time=[1], fruits=[[0, 3], [0, 5]], limit=2)
    print(ans)
