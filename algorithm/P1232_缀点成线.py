#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-30 23:32:32
LastEditTime: 2022-04-21 22:52:10
Description: 
FilePath: 1232.缀点成线.py
"""
#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][1] - coordinates[0][1] == 0:
            k = "inf"
        else:
            k = (coordinates[1][0] - coordinates[0][0]) / (
                coordinates[1][1] - coordinates[0][1]
            )

        for i in range(2, len(coordinates)):
            if coordinates[i][1] - coordinates[i - 1][1] == 0:
                cur_k = "inf"
            else:
                cur_k = (coordinates[i][0] - coordinates[i - 1][0]) / (
                    coordinates[i][1] - coordinates[i - 1][1]
                )
            if cur_k != k:
                return False
        return True


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(s.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
