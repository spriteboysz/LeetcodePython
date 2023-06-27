#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-23 20:47:18
LastEditTime: 2022-04-23 20:49:02
Description: 
FilePath: 991.坏了的计算器.py
"""


#
# @lc app=leetcode.cn id=991 lang=python3
#
# [991] 坏了的计算器
#

# @lc code=start
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while startValue < target:
            if target % 2 == 1:
                target += 1
            else:
                target //= 2
            count += 1
        return count + (startValue - target)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.brokenCalc(2, 3)
    print(ans)
