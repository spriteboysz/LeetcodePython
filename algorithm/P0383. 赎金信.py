#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-09-26 23:18:06
Description: 赎金信
FilePath: 383.赎金信.py
"""


#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if magazine.count(ch):
                magazine = magazine.replace(ch, "", 1)
            else:
                return False
        return True


# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct("a", "b"))
    print(s.canConstruct("aa", "ab"))
    print(s.canConstruct("aa", "aab"))
