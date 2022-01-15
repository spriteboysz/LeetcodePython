#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-15 23:44:29
LastEditTime: 2022-01-15 23:47:06
Description: 
FilePath: 657.机器人能否返回原点.py
'''
#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        countU, countD = moves.count("U"), moves.count("D")
        countL, countR = moves.count("L"), moves.count("R")
        return countU == countD and countL == countR

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.judgeCircle("LL"))
    
