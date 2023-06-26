#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-07 22:00:12
LastEditTime: 2022-02-07 22:08:16
Description:
FilePath: 2138.将字符串拆分为若干长度为-k-的组.py
"""
#
# @lc app=leetcode.cn id=2138 lang=python3
#
# [2138] 将字符串拆分为若干长度为 k 的组
#

# @lc code=start
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s) % k != 0:
            s += fill * (k - len(s) % k)
        divide = []
        for i in range(0, len(s) - k + 1, k):
            divide.append(s[i:i + k])
        return divide
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.divideString("abcdefghi", 3, "x"))
    print(s.divideString("abcdefghij", 3, "x"))
    print(s.divideString("hjefcvizjkecrioqhywe", 1, "s"))
