#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 21:43:53
LastEditTime: 2022-02-04 21:48:34
Description:
FilePath: 2235.将标题首字母大写.py
"""
#
# @lc app=leetcode.cn id=2235 lang=python3
#
# [2129] 将标题首字母大写
#

# @lc code=start


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.lower().strip().split()
        for i, word in enumerate(words):
            if len(word) > 2:
                words[i] = word.capitalize()
        return " ".join(words)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.capitalizeTitle("First leTTeR of EACH Word"))
    print(s.capitalizeTitle("i lOve leetcode"))
