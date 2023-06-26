#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-24 23:50:22
LastEditTime: 2022-01-25 00:02:14
Description:
FilePath: 1592.重新排列单词间的空格.py
"""
#
# @lc app=leetcode.cn id=1592 lang=python3
#
# [1592] 重新排列单词间的空格
#

# @lc code=start


class Solution:
    def reorderSpaces(self, text: str) -> str:
            words = text.strip().split()
            if len(words) == 1:
                return "".join(words) + " " * text.count(" ")
            else:
                div, mod = divmod(text.count(" "), len(words) - 1)
                return (" " * div).join(words) + " " * mod
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.reorderSpaces("a"))
    print(s.reorderSpaces("   hello"))
