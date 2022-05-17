#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-17 22:56:28
LastEditTime: 2022-05-17 23:00:51
Description: 
FilePath: 剑指 Offer II 037. 小行星碰撞.py
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack, i = [], 0
        while i < len(asteroids):
            if not stack or stack[-1] < 0 or asteroids[i] > 0:
                stack.append(asteroids[i])
            elif stack[-1] <= -asteroids[i]:
                if stack.pop() < -asteroids[i]:
                    continue
            i += 1
        return stack


if __name__ == "__main__":
    solution = Solution()
    ans = solution.asteroidCollision([-2, -1, 1, 2])
    print(ans)
    ans = solution.asteroidCollision([-2, -2, 1, -2])
    print(ans)
