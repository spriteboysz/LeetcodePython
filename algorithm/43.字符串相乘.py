#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-11 22:41:59
LastEditTime: 2022-01-11 22:44:31
Description: 字符串相乘
FilePath: 43.字符串相乘.py
'''
#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.multiply("123", "456"))
