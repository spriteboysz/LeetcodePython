#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-11 22:09
LastEditTime: 2022-06-11 22:09
Description:
FilePath: 55.跳跃游戏.py
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum = 0
        for i, jump in enumerate(nums):
            if maximum >= i and i + jump > maximum:
                maximum = i + jump
        return maximum >= len(nums) - 1


if __name__ == '__main__':
    solution = Solution()
    ans = solution.canJump(nums=[3, 2, 1, 0, 4])
    print(ans)
    ans = solution.canJump(nums = [2,3,1,1,4])
    print(ans)
