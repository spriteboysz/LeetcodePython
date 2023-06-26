#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-11 22:59:52
LastEditTime: 2022-02-11 23:05:07
Description:
FilePath: 1324.竖直打印单词.py
"""
#
# @lc app=leetcode.cn id=1324 lang=python3
#
# [1324] 竖直打印单词
#

# @lc code=start
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = max(map(len, words))
        words = list(map(lambda el: el + " " * (n - len(el)), words))
        return ["".join(el).rstrip() for el in zip(*words)]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.printVertically("TO BE OR NOT TO BE"))
    print(s.printVertically("HOW ARE YOU"))
    print(s.printVertically("CONTEST IS COMING"))
