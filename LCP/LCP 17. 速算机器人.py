#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-07 23:58:36
LastEditTime: 2022-02-08 00:00:33
Description: 
FilePath: 1000139.速算机器人.py
'''
#
# @lc app=leetcode.cn id=1000139 lang=python3
#
# [LCP 17] 速算机器人
#

# @lc code=start


class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for opt in s:
            if opt == "A":
                x = 2 * x + y
            elif opt == "B":
                y = 2 * y + x
        return x + y
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.calculate("AB"))
