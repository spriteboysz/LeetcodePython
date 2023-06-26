#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 23:55:09
LastEditTime: 2022-01-23 00:00:27
Description:
FilePath: 1903.字符串中的最大奇数.py
"""
#
# @lc app=leetcode.cn id=1903 lang=python3
#
# [1903] 字符串中的最大奇数
#

# @lc code=start


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
        return ""

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.largestOddNumber("35427"))
