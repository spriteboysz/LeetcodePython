#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-03 23:12:30
LastEditTime: 2022-02-03 23:19:11
Description: 
FilePath: 492.构造矩形.py
'''
#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for edge in range(int(area ** 0.5), -1, -1):
            if area % edge == 0:
                return [area // edge, edge]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.constructRectangle(6))
