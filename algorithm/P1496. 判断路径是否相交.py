#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-25 22:43:06
LastEditTime: 2022-01-25 22:49:10
Description: 
FilePath: 1496.判断路径是否相交.py
'''
#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#

# @lc code=start


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = [[0, 0]]
        x, y = 0, 0
        for item in path:
            if item == "N":
                y += 1
            elif item == "S":
                y -= 1
            elif item == "E":
                x += 1
            elif item == "W":
                x -= 1
            if [x, y] not in points:
                points.append([x, y])
            else:
                return True
        return False
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.isPathCrossing("NESWW"))
