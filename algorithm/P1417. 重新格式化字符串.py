#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 23:37:13
LastEditTime: 2022-01-25 23:48:32
Description:
FilePath: 1417.重新格式化字符串.py
"""


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
                for n, c in zip(num, letter):
                    s += n + c
                s += num[-1]
            elif len(letter) > len(num):
                for c, n in zip(letter, num):
                    s += c + n
                s += letter[-1]
            else:
                for c, n in zip(letter, num):
                    s += c + n
            return s


if __name__ == "__main__":
    s = Solution()
    print(s.reformat("a0b1c2"))
    print(s.reformat("l"))
    print(s.reformat("2"))
    print(s.reformat("covid2019"))
    print(s.reformat("ab123"))
