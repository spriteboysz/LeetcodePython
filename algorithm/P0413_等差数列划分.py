#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-23 17:14:21
LastEditTime: 2022-04-23 17:30:33
Description: 
FilePath: 413.等差数列划分.py
"""
#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diffs = []
        for i in range(1, len(nums)):
            diffs.append(nums[i] - nums[i - 1])
        print(diffs)

        cons, cur = [], 1
        for i in range(1, len(diffs)):
            if diffs[i] == diffs[i - 1]:
                cur += 1
            else:
                cons.append(cur)
                cur = 1
        cons.append(cur)

        count = 0
        for num in filter(lambda el: el > 1, cons):
            count += num * (num - 1) // 2
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numberOfArithmeticSlices([1, 2, 3, 4])
    print(ans)
    ans = solution.numberOfArithmeticSlices([1])
    print(ans)
