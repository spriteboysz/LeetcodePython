#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-11 22:08:21
LastEditTime: 2022-01-11 22:24:50
Description: 
FilePath: 17.电话号码的字母组合.py
'''
#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = [0, 1, "abc", "def", "ghi",
                    "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for item in list(digits):
            for i in keyboard[int(item)]:
                print(i)
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
