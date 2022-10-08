#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 21:47
LastEditTime: 2022-05-27 21:47
Description:
FilePath: 2278.字母在字符串中的百分比.py
"""


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.percentageLetter(s="foobar", letter="o")
    print(ans)
