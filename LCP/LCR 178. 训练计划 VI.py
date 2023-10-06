#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 23:14
FileName: LCP
Description:LCR 178. 训练计划 VI.py 
"""
from collections import defaultdict
from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        dic = defaultdict(int)
        for action in actions:
            dic[action] += 1
        for k, v in dic.items():
            if v == 1:
                return k


if __name__ == '__main__':
    print(Solution().trainingPlan(actions=[12, 1, 6, 12, 6, 12, 6]))
