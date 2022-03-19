#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 23:08:51
LastEditTime: 2022-03-19 23:17:20
Description: 
FilePath: 973.最接近原点的-k-个点.py
"""
#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#

# @lc code=start
from platform import java_ver
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis2 = [(i, j, i * i + j * j) for i, j in points]
        # dis2.sort(key=lambda el: el[2])
        return [[i, j] for i, j, _ in sorted(dis2, key=lambda el: el[2])[:k]]


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    ans = solution.kClosest(points=[[1, 3], [-2, 2]], k=1)
    print(ans)
    ans = solution.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2)
    print(ans)
