#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-20 21:58:41
LastEditTime: 2022-04-20 21:59:31
Description: 
FilePath: 2235.两整数相加.py
"""


#
# @lc app=leetcode.cn id=2235 lang=python3
#
# [2235] 两整数相加
#

# @lc code=start
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.sum(-10, 4)
    print(ans)
