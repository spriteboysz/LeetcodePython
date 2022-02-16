#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        s1 = n * n - sum([row.count(0) for row in grid])
        s2 = sum([max(row) for row in grid])
        s3 = sum([max(col) for col in zip(*grid)])
        return s1 + s2 + s3


# @lc code=end
