#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-23 22:26:46
LastEditTime: 2022-02-23 22:29:15
Description: 
FilePath: 633.平方数之和.py
"""
#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # b2 = [i * i for i in range(int(c ** 0.5) + 1)]
        for a in range(int(c ** 0.5) + 1):
            if (c - a * a) ** 0.5 % 1 == 0:
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.judgeSquareSum(2147482647)
    print(ans)
