#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-17 23:16:35
LastEditTime: 2022-03-17 23:32:10
Description:
FilePath: 13.罗马数字转整数.py
"""


#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ss = 0
        src = ["IV", "IX", "XL", "XC", "CD", "CM", "V", "L", "D",
               "III", "II", "I", "XXX", "XX", "X", "CCC", "CC", "C", "MMM", "MM", "M"]
        dst = [4, 9, 40, 90, 400, 900, 5, 50, 500,
               3, 2, 1, 30, 20, 10, 300, 200, 100, 3000, 2000, 1000]
        for i in range(len(src)):
            if s.count(src[i]):
                s = s.replace(src[i], "")
                ss += dst[i]

        return ss


# @lc code=end


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("LVIII"))
