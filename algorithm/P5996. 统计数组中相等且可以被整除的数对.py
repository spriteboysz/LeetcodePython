#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-01 23:20:22
LastEditTime: 2022-03-01 23:33:33
Description: 
FilePath: 5996.统计数组中相等且可以被整除的数对.py
"""
#
# @lc app=leetcode.cn id=5996 lang=python3
#
# [5996] 统计数组中相等且可以被整除的数对
#

# @lc code=start
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2)
    print(ans)
