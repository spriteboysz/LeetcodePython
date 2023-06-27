#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 22:16:12
LastEditTime: 2022-04-13 22:24:17
Description: 
FilePath: 6035.选择建筑的方案数.py
"""


#
# @lc app=leetcode.cn id=6035 lang=python3
#
# [6035] 选择建筑的方案数
#

# @lc code=start
class Solution:
    def numberOfWays(self, s: str) -> int:
        l0, l1, n0, n1, count = 0, 0, s.count("0"), s.count("1"), 0
        for item in s:
            if item == "0":
                l0 += 1
                count += l1 * (n1 - l1)
            else:
                l1 += 1
                count += l0 * (n0 - l0)
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numberOfWays("001101")
    print(ans)
    ans = solution.numberOfWays("111000")
    print(ans)
