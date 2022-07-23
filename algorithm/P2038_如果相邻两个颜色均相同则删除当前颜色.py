#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-24 23:09:28
LastEditTime: 2022-02-24 23:12:36
Description: 
FilePath: 2038.如果相邻两个颜色均相同则删除当前颜色.py
"""
#
# @lc app=leetcode.cn id=2038 lang=python3
#
# [2038] 如果相邻两个颜色均相同则删除当前颜色
#

# @lc code=start
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice, bob = 0, 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1 : i + 2] == "AAA":
                alice += 1
            elif colors[i - 1 : i + 2] == "BBB":
                bob += 1
        return alice > bob


# @lc code=end
