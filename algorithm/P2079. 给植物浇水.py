#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-15 22:56:10
LastEditTime: 2022-02-15 23:06:03
Description:
FilePath: 2079.给植物浇水.py
"""
#
# @lc app=leetcode.cn id=2079 lang=python3
#
# [2079] 给植物浇水
#

# @lc code=start
from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count, cur = 0, capacity
        for i, plant in enumerate(plants):
            if cur >= plant:
                cur -= plant
                count += 1
            else:
                cur = capacity - plant
                count += i + i + 1
        return count

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.wateringPlants([2, 2, 3, 3], 5))
    print(s.wateringPlants([1, 1, 1, 4, 2, 3], 4))
    print(s.wateringPlants([7, 7, 7, 7, 7, 7, 7], 8))
