#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 23:10
FileName: algorithm/P2432. 处理用时最长的那个任务的员工.py
Description: 
"""
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        if n < len(logs):
            return 0
        worker = []
        cur = 0
        for index, end in logs:
            worker.append([index, end - cur])
            cur = end
        worker.sort(key=lambda el: (-el[1], el[0]))
        return worker[0][0]


if __name__ == '__main__':
    # print(Solution().hardestWorker(n=10, logs=[[0, 3], [2, 5], [0, 9], [1, 15]]))
    n = 70
    logs = [[36, 3], [1, 5], [12, 8], [25, 9], [53, 11], [29, 12], [52, 14]]
    print(Solution().hardestWorker(n, logs))
