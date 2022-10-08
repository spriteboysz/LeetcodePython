#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-04 22:12:53
LastEditTime: 2022-04-04 22:19:45
Description: 
FilePath: 2208.将数组和减半的最少操作次数.py
"""
#
# @lc app=leetcode.cn id=2208 lang=python3
#
# [2208] 将数组和减半的最少操作次数
#

from heapq import heappop, heappush
# @lc code=start
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap, sum_ = [], 0
        for num in nums:
            heappush(heap, -num)
            sum_ += num

        target, sum_, count = sum_ / 2, 0, 0
        while sum_ < target:
            cur = heappop(heap) / 2
            heappush(heap, cur)
            sum_ += -cur
            count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.halveArray([5, 19, 8, 1])
    print(ans)
