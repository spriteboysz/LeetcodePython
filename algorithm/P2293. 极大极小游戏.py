#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-09 23:26
LastEditTime: 2022-06-09 23:26
Description:
FilePath: 2293.极大极小游戏.py
"""

from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n != 1:
            for i in range(n // 2):
                if i % 2 == 0:
                    nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i] = max(nums[2 * i], nums[2 * i + 1])
            n //= 2
        return nums[0]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.minMaxGame(nums=[1, 3, 5, 2, 4, 8, 2, 2])
    print(ans)
