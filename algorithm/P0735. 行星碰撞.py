#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-03 23:00:37
LastEditTime: 2022-03-03 23:08:48
Description: 
FilePath: 735.行星碰撞.py
"""
#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#

# @lc code=start
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 > asteroid:
                pre = stack.pop()
                if abs(pre) > abs(asteroid):
                    stack.append(pre)
                    asteroid = 0
                    break
                elif abs(pre) == abs(asteroid):
                    asteroid = 0
                    break
            if asteroid:
                stack.append(asteroid)
        return stack


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.asteroidCollision([5, 10, -5])
    print(ans)
