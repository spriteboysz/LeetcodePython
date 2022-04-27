#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-27 21:43:46
LastEditTime: 2022-04-27 21:54:39
Description: 
FilePath: 1222.可以攻击国王的皇后.py
"""
#
# @lc app=leetcode.cn id=1222 lang=python3
#
# [1222] 可以攻击国王的皇后
#

# @lc code=start
from typing import List


class Solution:
    def queensAttacktheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        result = []
        # 从国王出发
        # 判断国王的竖直方向，水平方向，对角线方向是否有黑皇后
        directions = [(1, 0), (1, 1), (0, 1), (-1, -1), (1, -1), (0, -1), (-1, 1), (-1, 0)]
        for i, j in directions:
            x, y = king
            while 0 <= x < 8 and 0 <= y < 8:
                if [x + i, y + j] in queens:
                    result.append([x + i, y + j])
                    break
                x += i
                y += j
        return result


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.queensAttacktheKing(
        queens=[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], king=[0, 0]
    )
    print(ans)
