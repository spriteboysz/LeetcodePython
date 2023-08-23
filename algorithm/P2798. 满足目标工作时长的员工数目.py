#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-22 23:57
FileName: algorithm
Description:P2798. 满足目标工作时长的员工数目.py 
"""
from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len(list(filter(lambda el: el >= target, hours)))


if __name__ == '__main__':
    print(Solution().numberOfEmployeesWhoMetTarget(hours=[0, 1, 2, 3, 4], target=2))
