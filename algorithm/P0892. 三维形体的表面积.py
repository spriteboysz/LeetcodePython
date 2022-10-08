#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-25 23:23:40
LastEditTime: 2022-04-25 23:25:17
Description: 
FilePath: 892.三维形体的表面积.py
"""
#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

# @lc code=start
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        # 先算不遮挡的总表面积，再减去遮挡的面积
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] > 0:
                    # 每一个都看做一个高=grid[i][j]的柱体，有两个底和四个侧面
                    area += grid[i][j] * 4 + 2
                # 相邻的两个柱体之间遮挡了min(两个柱体的高)*2
                if i > 0:
                    area -= min(grid[i][j], grid[i - 1][j]) * 2
                if j > 0:
                    area -= min(grid[i][j], grid[i][j - 1]) * 2
        return area


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.surfaceArea(grid=[[1, 2], [3, 4]])
    print(ans)
