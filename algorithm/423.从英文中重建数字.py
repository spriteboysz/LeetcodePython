#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-19 22:30:31
LastEditTime: 2022-02-19 22:50:40
Description: 
FilePath: 423.从英文中重建数字.py
"""
#
# @lc app=leetcode.cn id=423 lang=python3
#
# [423] 从英文中重建数字
#

# @lc code=start
from collections import defaultdict


class Solution:
    def originalDigits(self, s: str) -> str:
        # words = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "night"]
        # number = defaultdict(set)
        # for i, word in enumerate(words):
        #     for letter in word:
        #         number[letter].add(i)
        # print(number)
        letters = defaultdict(int)
        for item in s:
            letters[item] += 1

        counts = [0] * 10
        counts[0] = letters.get("z", 0)
        counts[2] = letters.get("w", 0)
        counts[4] = letters.get("u", 0)
        counts[6] = letters.get("x", 0)
        counts[5] = letters.get("f", 0) - counts[4]
        counts[7] = letters.get("v", 0) - counts[5]
        counts[1] = letters.get("o", 0) - counts[0] - counts[2] - counts[4]
        counts[9] = (letters.get("n", 0) - counts[1] - counts[7]) // 2
        counts[8] = letters.get("i", 0) - counts[5] - counts[6] - counts[9]
        counts[3] = letters.get("h", 0) - counts[8]
        return "".join(str(i) * counts[i] for i in range(10))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.originalDigits("owoztneoer")
    ans = solution.originalDigits("fviefuro")
    print(ans)
