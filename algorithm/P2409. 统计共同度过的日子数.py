#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 23:31
FileName: algorithm/P2409. 统计共同度过的日子数.py
Description: 
"""


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def process(date):
            mm, days = map(int, date.split("-"))
            for i in range(mm - 1):
                days += month[i]
            return days

        return max(0, min(process(leaveAlice), process(leaveBob)) - max(process(arriveAlice), process(arriveBob)) + 1)


if __name__ == '__main__':
    arriveAlice = "08-15"
    leaveAlice = "08-18"
    arriveBob = "08-16"
    leaveBob = "08-19"
    print(Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
