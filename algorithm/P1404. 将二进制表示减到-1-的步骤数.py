#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-07 23:47:38
LastEditTime: 2022-04-07 23:49:34
Description: 
FilePath: 1404.将二进制表示减到-1-的步骤数.py
"""


#
# @lc app=leetcode.cn id=1404 lang=python3
#
# [1404] 将二进制表示减到 1 的步骤数
#

# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, base=2)
        count = 0
        while num != 1:
            count += 1
            if num % 2 == 0:
                num //= 2
            else:
                num += 1

        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numSteps("10")
    print(ans)
