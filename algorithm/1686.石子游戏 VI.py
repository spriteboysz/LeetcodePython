#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 17:13
LastEditTime: 2022-05-29 17:13
Description:
FilePath: 1686.石子游戏 VI.py
"""

from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        total = sorted(
            [a + b for a, b in zip(aliceValues, bobValues)], reverse=True)
        game = sum(total[::2]) - sum(bobValues)
        if game > 0:
            return 1
        elif game < 0:
            return -1
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    ans = solution.stoneGameVI([1, 3], [2, 1])
    print(ans)
    ans = solution.stoneGameVI([2,4,3], [1,6,7])
    print(ans)