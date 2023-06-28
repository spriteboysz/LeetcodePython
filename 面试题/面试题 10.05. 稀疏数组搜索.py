#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 22:57:24
LastEditTime: 2022-02-04 22:58:40
Description:
FilePath: 100242.稀疏数组搜索.py
"""
#
# @lc app=leetcode.cn id=100242 lang=python3
#
# [面试题 10.05] 稀疏数组搜索
#

# @lc code=start
from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for i, word in enumerate(words):
            if word == s:
                return i
        return -1
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.findString(words=["at", "", "", "", "ball",
          "", "", "car", "", "", "dad", "", ""], s="ball"))
