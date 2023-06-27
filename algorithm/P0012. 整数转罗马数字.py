#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 14:02:32
LastEditTime: 2022-04-10 14:06:01
Description: 
FilePath: 12.整数转罗马数字.py
"""


#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        transform = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        roman = ""
        for key, value in transform.items():
            if num // key != 0:
                count, num = divmod(num, key)
                roman += value * count
        return roman


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.intToRoman(3999)
    print(ans)
