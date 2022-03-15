#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-15 19:01:59
LastEditTime: 2022-03-15 19:03:45
Description: 
FilePath: 686.重复叠加字符串匹配.py
"""
#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#

# @lc code=start
from math import ceil


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        multiple = ceil(len(b) / len(a))
        if b in a * multiple:
            return multiple
        elif b in a * (multiple + 1):
            return multiple + 1
        else:
            return -1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.repeatedStringMatch(a="abcd", b="cdabcdab")
    print(ans)
