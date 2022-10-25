#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-25 23:55
FileName: algorithm/P2309. 兼具大小写的最好英文字母.py
Description: 
"""
from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase


class Solution:
    def greatestLetter(self, s: str) -> str:
        for lower, upper in zip(reversed(lowercase), reversed(uppercase)):
            if lower in s and upper in s:
                return upper
        return ""


if __name__ == '__main__':
    print(Solution().greatestLetter("arRAzFif"))
    print(Solution().greatestLetter("AbCdEfGhIjK"))
