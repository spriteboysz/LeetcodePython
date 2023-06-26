#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-09 21:24:22
LastEditTime: 2022-02-09 21:37:16
Description:
FilePath: 1881.插入后的最大值.py
"""
#
# @lc app=leetcode.cn id=1881 lang=python3
#
# [1881] 插入后的最大值
#

# @lc code=start
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n.startswith("-"):
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    position = i
                    break
            else:
                position = len(n)
        else:
            for i in range(len(n)):
                if int(n[i]) < x:
                    position = i
                    break
            else:
                position = len(n)
        return n[:position] + str(x) + n[position:]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxValue("87", 9))
    print(s.maxValue("-132", 3))
    print(s.maxValue("-13", 2))
