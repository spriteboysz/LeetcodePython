#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 23:41:29
LastEditTime: 2022-03-05 23:52:51
Description: 
FilePath: 1267.统计参与通信的服务器.py
"""
#
# @lc app=leetcode.cn id=1267 lang=python3
#
# [1267] 统计参与通信的服务器
#

# @lc code=start
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = [sum(r) for r in grid]
        column = [sum(c) for c in zip(*grid)]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (row[i] >= 2 or column[j] >= 2):
                    count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.countServers([[1, 0], [0, 1]])
    print(ans)
    ans = solution.countServers([[1, 0], [1, 1]])
    print(ans)
    ans = solution.countServers(
        grid=[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    )
    print(ans)
