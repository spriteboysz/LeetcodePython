#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-09 22:32:30
LastEditTime: 2022-02-12 17:55:19
Description:
FilePath: 1641.统计字典序元音字符串的数目.py
"""
#
# @lc app=leetcode.cn id=1641 lang=python3
#
# [1641] 统计字典序元音字符串的数目
#

# @lc code=start
from itertools import combinations_with_replacement


class Solution:
    def countVowelStrings(self, n: int) -> int:
        # * python内置全排列工具
        return len(list(combinations_with_replacement("aeiou", n)))


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.countVowelStrings(2))
