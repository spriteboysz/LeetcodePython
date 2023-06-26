#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-30 22:59:55
LastEditTime: 2022-01-30 23:10:12
Description:
FilePath: 1576.替换所有的问号.py
"""
#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def modifyString(self, s: str) -> str:
        s = list("#" + s + "#")
        for i in range(1, len(s) - 1):
            if s[i] == "?":
                for letter in ascii_lowercase:
                    if s[i - 1] != letter and s[i + 1] != letter:
                        s[i] = letter
                        break
        return "".join(s[1:-1])
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.modifyString("j?qg??b"))
