#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-04 22:26:05
Description: 
FilePath: 1812.判断国际象棋棋盘中一个格子的颜色.py
'''
#
# @lc app=leetcode.cn id=1812 lang=python3
#
# [1812] 判断国际象棋棋盘中一个格子的颜色
#

# @lc code=start


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        co = ord(coordinates[0]) + int(coordinates[1])
        return co % 2 != 0

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.squareIsWhite("a1"))
