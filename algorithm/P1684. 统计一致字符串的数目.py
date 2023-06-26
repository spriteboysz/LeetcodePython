#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 22:36:31
LastEditTime: 2022-01-23 22:39:47
Description:
FilePath: 1684.统计一致字符串的数目.py
"""
#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#

# @lc code=start
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            for letter in set(word):
                if letter not in allowed:
                    break
            else:
                count += 1
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.countConsistentStrings(
        "abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
