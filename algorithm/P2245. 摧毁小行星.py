#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-08 22:12:30
LastEditTime: 2022-02-08 22:15:30
Description:
FilePath: 2245.摧毁小行星.py
"""
#
# @lc app=leetcode.cn id=2245 lang=python3
#
# [2126] 摧毁小行星
#

# @lc code=start
from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for asteroid in sorted(asteroids):
            if mass < asteroid:
                return False
            else:
                mass += asteroid
        return True
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.asteroidsDestroyed(mass=5, asteroids=[4, 9, 23, 4]))
