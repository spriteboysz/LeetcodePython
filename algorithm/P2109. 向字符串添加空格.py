#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-18 22:11:27
LastEditTime: 2022-02-18 22:15:14
Description: 
FilePath: 2109.向字符串添加空格.py
"""
#
# @lc app=leetcode.cn id=2109 lang=python3
#
# [2109] 向字符串添加空格
#

# @lc code=start
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        for start, end in zip([0] + spaces, spaces + [len(s)]):
            words.append(s[start:end])
        return " ".join(words)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.addSpaces(s="icodeinpython", spaces=[1, 5, 7, 9])
    print(ans)
    ans = solution.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15])
    print(ans)
