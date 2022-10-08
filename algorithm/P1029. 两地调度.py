#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-17 22:50:35
LastEditTime: 2022-02-17 22:55:25
Description: 
FilePath: 1029.两地调度.py
"""
#
# @lc app=leetcode.cn id=1029 lang=python3
#
# [1029] 两地调度
#

# @lc code=start
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs = sorted(costs, key=lambda el: (el[0] - el[1]))
        return sum(map(lambda el: el[0], costs[:n])) + sum(
            map(lambda el: el[1], costs[n:])
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]])
    print(ans)
