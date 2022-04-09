#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 22:02:45
LastEditTime: 2022-04-09 22:04:46
Description: 
FilePath: 767.重构字符串.py
"""
#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#

# @lc code=start
from collections import defaultdict


class Solution:
    def reorganizeString(self, s: str) -> str:
        lettercount, n = defaultdict(int), len(s)
        for letter in s:
            lettercount[letter] += 1

        if max(lettercount.values()) > (n + 1) // 2:
            return ""
        reorganize = []
        for k, v in sorted(lettercount.items(), key=lambda el: -el[1]):
            reorganize.extend([k] * v)

        reorganize[::2], reorganize[1::2] = (
            reorganize[: (n + 1) // 2],
            reorganize[(n + 1) // 2 :],
        )
        return "".join(reorganize)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.reorganizeString("abb")
    print(ans)
