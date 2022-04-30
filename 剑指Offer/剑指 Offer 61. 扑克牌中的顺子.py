#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-30 23:08:49
LastEditTime: 2022-04-30 23:10:01
Description: 
FilePath: 剑指 Offer 61. 扑克牌中的顺子.py
"""

from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        maximum, minimum = 0, 14
        repeat = set()
        for num in filter(lambda el: el != 0, nums):
            maximum = max(maximum, num)
            minimum = min(minimum, num)
            if num in repeat:
                return False
            repeat.add(num)
        return maximum - minimum < 5


if __name__ == "__main__":
    solution = Solution()
    ans = solution.isStraight([1, 2, 3, 4, 5])
    print(ans)
    ans = solution.isStraight([0, 0, 0, 0, 13])
    print(ans)
