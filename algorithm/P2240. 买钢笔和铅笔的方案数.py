#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-24 23:20:47
LastEditTime: 2022-04-24 23:22:52
Description: 
FilePath: 2240.买钢笔和铅笔的方案数.py
"""


#
# @lc app=leetcode.cn id=2240 lang=python3
#
# [2240] 买钢笔和铅笔的方案数
#

# @lc code=start
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        count = 0
        for i in range(total // cost1 + 1):
            count += (total - i * cost1) // cost2 + 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.waysToBuyPensPencils(20, 10, 5)
    print(ans)
    ans = solution.waysToBuyPensPencils(5, 10, 10)
    print(ans)
    ans = solution.waysToBuyPensPencils(1000000, 1, 1)
    print(ans)  # 500001500001
