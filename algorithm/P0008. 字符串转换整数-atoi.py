#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-18 23:45:48
LastEditTime: 2022-02-19 00:03:48
Description: 
FilePath: 8.字符串转换整数-atoi.py
"""


#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if s.strip() == "":
            return 0

        s = s.strip().split()[0]
        negative, num = False, 0
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        for item in s:
            if item.isdigit():
                num = num * 10 + int(item)
                if num > 2 ** 32:
                    num = 2 ** 32
                    break
            else:
                break
        if negative:
            num = -num
        if num >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif num <= -(2 ** 31):
            return -(2 ** 31)
        else:
            return num


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.myAtoi("")
    print(ans)
    ans = solution.myAtoi("   ")
    print(ans)
