#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 23:30:16
LastEditTime: 2022-02-16 23:33:40
Description: 
FilePath: 2169.得到-0-的操作数.py
"""


#
# @lc app=leetcode.cn id=2169 lang=python3
#
# [2169] 得到 0 的操作数
#

# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        if num1 < num2:
            num1, num2 = num2, num1
        while num1 and num2:
            div, mod = divmod(num1, num2)
            count += div
            num1, num2 = num2, mod
        return count


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.countOperations(100, 1)
    print(ans)
