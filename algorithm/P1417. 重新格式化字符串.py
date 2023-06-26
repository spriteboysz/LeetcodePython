#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 23:37:13
LastEditTime: 2022-01-25 23:48:32
Description:
FilePath: 1417.重新格式化字符串.py
"""
#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start


class Solution:
    def reformat(self, s: str) -> str:
        num, letter = [], []
        for item in s:
            if item.isdigit():
                num.append(item)
            elif item.isalpha():
                letter.append(item)
        s = ""
        if abs(len(num) - len(letter)) > 1:
            return s
        else:
            if len(num) > len(letter):
                for n, l in zip(num, letter):
                    s += n + l
                s += num[-1]
            elif len(letter) > len(num):
                for l, n in zip(letter, num):
                    s += l + n
                s += letter[-1]
            else:
                for l, n in zip(letter, num):
                    s += l + n
            return s

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.reformat("a0b1c2"))
    print(s.reformat("l"))
    print(s.reformat("2"))
    print(s.reformat("covid2019"))
    print(s.reformat("ab123"))
