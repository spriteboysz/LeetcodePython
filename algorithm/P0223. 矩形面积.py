#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-09 23:16:39
LastEditTime: 2022-02-09 23:22:19
Description: 
FilePath: 223.矩形面积.py
'''
#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#

# @lc code=start


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        s1 = (ax2 - ax1) * (ay2 - ay1)
        s2 = (bx2 - bx1) * (by2 - by1)
        s3 = max(min(ax2, bx2) - max(ax1, bx1), 0) * \
            max(min(ay2, by2) - max(ay1, by1), 0)
        return s1 + s2 - s3
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.computeArea(ax1=-2, ay1=-2, ax2=2,
          ay2=2, bx1=-2, by1=-2, bx2=2, by2=2))
