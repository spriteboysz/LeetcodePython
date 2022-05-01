#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 23:23:38
LastEditTime: 2022-05-01 23:28:38
Description: 
FilePath: 面试题 16.15. 珠玑妙算.py
"""

from typing import List


class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        hit, count = 0, 0
        for s, g in zip(solution, guess):
            hit += int(s == g)

        for color in ["R", "G", "B", "Y"]:
            count += min(solution.count(color), guess.count(color))

        return [hit, count - hit]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.masterMind(solution="RRGG", guess="GGRR")
    print(ans)
