#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-17 23:14:54
LastEditTime: 2022-01-17 23:27:06
Description: 
FilePath: 836.矩形重叠.py
'''
#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#

# @lc code=start
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1 = max(rec1[0], rec2[0]), max(rec1[1], rec2[1])
        x2, y2 = min(rec1[2], rec2[2]), min(rec1[3], rec2[3])

        return True if x1 < x2 and y1 < y2 else False


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]))
