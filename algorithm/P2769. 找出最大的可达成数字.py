#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-10 22:55
FileName: algorithm/P2769. 找出最大的可达成数字.py
Description: 
"""


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2


if __name__ == '__main__':
    print(Solution().theMaximumAchievableX(num=3, t=2))
