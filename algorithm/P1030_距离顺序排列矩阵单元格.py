#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-02 22:13:27
LastEditTime: 2022-02-02 22:24:44
Description: 
FilePath: 1030.距离顺序排列矩阵单元格.py
'''
#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        distance = dict()
        for i in range(rows):
            for j in range(cols):
                cur = abs(rCenter - i) + abs(cCenter - j)
                if cur in distance.keys():
                    distance[cur].append([i, j])
                else:
                    distance[cur] = [[i, j]]
        order = []
        for item in sorted(distance.keys()):
            order.extend(distance[item])
        return order

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.allCellsDistOrder(1, 2, 0, 0))
    print(s.allCellsDistOrder(2, 2, 0, 1))
    print(s.allCellsDistOrder(2, 3, 1, 2))
