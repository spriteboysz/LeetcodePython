#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 23:45
FileName: LCP
Description:LCR 186. 文物朝代判断.py 
"""
from typing import List


class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        unknown = 0
        places.sort()
        for i in range(4):
            if places[i] == 0:
                unknown += 1
            elif places[i] == places[i + 1]:
                return False
        return places[4] - places[unknown] < 5


if __name__ == '__main__':
    print(Solution().checkDynasty(places=[0, 6, 9, 0, 7]))
