#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-01 21:13
FileName: algorithm
Description:P2895. 最小处理时间.py 
"""
from typing import List


class Solution:
    def minProcessingTime(self, processor_time: List[int], tasks: List[int]) -> int:
        processor_time.sort()
        tasks.sort(reverse=True)
        return max([p + t for p, t in zip(processor_time, tasks[::4])])


if __name__ == '__main__':
    print(Solution().minProcessingTime(processor_time=[8, 10], tasks=[2, 2, 3, 1, 8, 7, 4, 5]))
