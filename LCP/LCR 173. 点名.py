#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 23:06
FileName: LCP
Description:LCR 173. 点名.py 
"""
from typing import List


class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        for i, record in enumerate(records):
            if i != record:
                return i
        return len(records)


if __name__ == '__main__':
    print(Solution().takeAttendance(records=[1, 2, 3, 4, 5, 6, 7, 8]))
