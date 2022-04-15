#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-15 22:58:51
LastEditTime: 2022-04-15 23:06:10
Description: 
FilePath: 1792.最大平均通过率.py
"""
#
# @lc app=leetcode.cn id=1792 lang=python3
#
# [1792] 最大平均通过率
#

# @lc code=start
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for pi, ti in classes:
            heappush(heap, [(pi - ti) / (ti + 1) / ti, pi, ti])

        for _ in range(extraStudents):
            _, pi, ti = heappop(heap)
            pi, ti = pi + 1, ti + 1
            heappush(heap, [(pi - ti) / (ti + 1) / ti, pi, ti])

        return sum([heap[i][1] / heap[i][2] for i in range(len(classes))]) / len(
            classes
        )


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2)
    print(ans)
