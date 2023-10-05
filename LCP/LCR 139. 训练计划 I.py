#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:15
FileName: LCP
Description:LCR 139. 训练计划 I.py 
"""
from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        return sorted(actions, key=lambda el: el % 2, reverse=True)


if __name__ == '__main__':
    print(Solution().trainingPlan(actions=[1, 2, 3, 4, 5]))
