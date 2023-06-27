#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-11 16:09
LastEditTime: 2022-06-11 16:09
Description:
FilePath: 面试题 17.08. 马戏团人塔.py
"""

from bisect import bisect_left
from typing import List


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        dp = []
        for h, w in sorted(zip(height, weight),
                           key=lambda el: (el[0], -el[1])):
            position = bisect_left(dp, w)
            dp[position:position + 1] = [w]
            # print(dp)
        return len(dp)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.bestSeqAtIndex(
        height=[
            65, 70, 56, 75, 60, 68], weight=[
            100, 150, 90, 190, 95, 110])
    print(ans)
