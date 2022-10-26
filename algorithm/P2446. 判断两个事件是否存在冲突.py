#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 22:37
FileName: algorithm/P2446. 判断两个事件是否存在冲突.py
Description: 
"""
from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def process(time):
            hh, mm = map(int, time.split(":"))
            return hh * 60 + mm

        start1, end1 = map(process, event1)
        start2, end2 = map(process, event2)
        return start1 <= end2 and start2 <= end1


if __name__ == '__main__':
    print(Solution().haveConflict(["01:00", "02:00"], ["01:20", "03:00"]))
    print(Solution().haveConflict(["10:00", "11:00"], ["14:00", "15:00"]))
