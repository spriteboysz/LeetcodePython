#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-02 21:01:20
LastEditTime: 2022-05-02 21:01:20
Description: 
FilePath: 面试题 16.20. T9键盘.py
"""

from typing import List
from string import ascii_lowercase as lower


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        keyboard = [
            2,
            2,
            2,
            3,
            3,
            3,
            4,
            4,
            4,
            5,
            5,
            5,
            6,
            6,
            6,
            7,
            7,
            7,
            7,
            8,
            8,
            8,
            9,
            9,
            9,
            9,
        ]
        hit = []
        for word in filter(lambda el: len(el) == len(num), words):
            cur = ""
            for letter in word:
                cur += str(keyboard[lower.index(letter)])
            if cur == num:
                hit.append(word)
        return hit


if __name__ == "__main__":
    solution = Solution()
    ans = solution.getValidT9Words(num="8733", words=["tree", "abcd", "used"])
    print(ans)
