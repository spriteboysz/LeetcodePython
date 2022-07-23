#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 12:33:57
LastEditTime: 2022-02-04 12:41:23
Description: 
FilePath: 682.棒球比赛.py
'''
#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for operator in ops:
            if operator == "+":
                score.append(score[-1] + score[-2])
            elif operator == "D":
                score.append(2 * score[-1])
            elif operator == "C":
                score.pop()
            else:
                score.append(int(operator))
        return sum(score)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
