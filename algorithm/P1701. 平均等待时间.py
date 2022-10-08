#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 17:29
LastEditTime: 2022-05-29 17:29
Description:
FilePath: 1701.平均等待时间.py
"""

from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait, free = 0, 0
        for arrive, cost in customers:
            if free <= arrive:
                free = arrive + cost
                wait += cost
            else:
                free += cost
                wait += (free - arrive)
        return wait / len(customers)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.averageWaitingTime(
        customers=[[5, 2], [5, 4], [10, 3], [20, 1]])
    print(ans)
