#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-01 22:07:58
LastEditTime: 2022-02-01 22:09:26
Description:
FilePath: 28.实现-str-str.py
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("hello", "ll"))
    print(s.strStr("aaaaa", "bba"))
    print(s.strStr("", ""))
