#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-22 23:39:01
LastEditTime: 2022-04-22 23:41:36
Description: 
FilePath: 1513.仅含-1-的子串数.py
"""


#
# @lc app=leetcode.cn id=1513 lang=python3
#
# [1513] 仅含 1 的子串数
#

# @lc code=start
class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        for item in filter(lambda el: el != "", s.split("0")):
            n = len(item)
            count += (n + 1) * n
        return (count // 2) % (10 ** 9 + 7)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.numSub("0110111")
    print(ans)
