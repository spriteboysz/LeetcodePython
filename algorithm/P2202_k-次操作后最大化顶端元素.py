#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 22:44:22
LastEditTime: 2022-04-13 22:50:33
Description: 
FilePath: 2202.k-次操作后最大化顶端元素.py
"""
#
# @lc app=leetcode.cn id=2202 lang=python3
#
# [2202] K 次操作后最大化顶端元素
#

# @lc code=start
from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) > 1 or k % 2 == 0:
            return max(num for i, num in enumerate(nums) if i < k - 1 or i == k)
        else:
            return -1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maximumTop(nums=[5, 2, 2, 4, 0, 6], k=4)
    print(ans)
