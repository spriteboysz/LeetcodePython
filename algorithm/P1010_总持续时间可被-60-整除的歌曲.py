#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-27 16:07:21
LastEditTime: 2022-02-27 16:10:32
Description: 
FilePath: 1010.总持续时间可被-60-整除的歌曲.py
"""
#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#

from collections import defaultdict
# @lc code=start
from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder = defaultdict(int)
        for item in time:
            remainder[item % 60] += 1
        # print(remainder)
        count = 0
        for i in range(31):
            if i == 0 or i == 30:
                count += remainder[i] * (remainder[i] - 1) // 2
            else:
                count += remainder[i] * remainder[60 - i]
        return count


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.numPairsDivisibleBy60([30, 20, 150, 100, 40])
    print(ans)
    ans = solution.numPairsDivisibleBy60([60, 60, 60])
    print(ans)