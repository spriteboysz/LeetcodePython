#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-07 23:15:46
LastEditTime: 2022-04-07 23:22:03
Description: 
FilePath: 1390.四因数.py
"""
#
# @lc app=leetcode.cn id=1390 lang=python3
#
# [1390] 四因数
#

# @lc code=start
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        if len(nums) == 1:
            upper = nums[0]
        else:
            upper = max(*nums)
        number = [0 for i in range(upper + 1)]
        cur = [0 for i in range(upper + 1)]
        for i in range(1, upper + 1):
            for j in range(i, upper + 1, i):
                number[j] += 1
                cur[j] += i

        sum_ = 0
        for num in nums:
            if number[num] == 4:
                sum_ += cur[num]

        return sum_


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.sumFourDivisors([])
    print(ans)
