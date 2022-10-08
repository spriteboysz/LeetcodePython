#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-12 23:59:17
LastEditTime: 2022-04-13 00:00:53
Description: 
FilePath: 6039.k-次增加后的最大乘积.py
"""
#
# @lc app=leetcode.cn id=6039 lang=python3
#
# [6039] K 次增加后的最大乘积
#

# @lc code=start
from heapq import heapify, heapreplace
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(k):
            heapreplace(nums, nums[0] + 1)

        product = 1
        for num in nums:
            product = (product * num) % (10 ** 9 + 7)
        return product


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maximumProduct([0, 4], 5)
    print(ans)
