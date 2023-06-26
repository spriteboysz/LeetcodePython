#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 21:32:29
LastEditTime: 2022-01-28 21:39:33
Description:
FilePath: 1189.气球-的最大数量.py
"""
#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        return min([text.count(letter) // ballon[letter] for letter in ballon.keys()])

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxNumberOfBalloons("loonbalxballpoon"))
    print(s.maxNumberOfBalloons("leetcode"))
