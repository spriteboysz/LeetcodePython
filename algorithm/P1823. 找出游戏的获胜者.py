#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-12 21:45:05
LastEditTime: 2022-03-12 21:48:12
Description: 
FilePath: 1823.找出游戏的获胜者.py
"""


#
# @lc app=leetcode.cn id=1823 lang=python3
#
# [1823] 找出游戏的获胜者
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        start, circle = 0, [i for i in range(1, n + 1)]
        while len(circle) > 1:
            loss = (start + k - 1) % len(circle)
            start = 0 if loss == len(circle) - 1 else loss
            circle.pop(loss)
        return circle[0]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findTheWinner(5, 2)
    print(ans)
    ans = solution.findTheWinner(6, 5)
    print(ans)
