#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 23:00:27
LastEditTime: 2022-01-28 23:07:34
Description:
FilePath: 744.寻找比目标字母大的最小字母.py
"""
#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if ord(target) < ord(letter):
                return letter
        return letters[0]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.nextGreatestLetter(["c", "f", "j"], "j"))
