#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-19 23:18:01
LastEditTime: 2022-02-19 23:21:31
Description: 
FilePath: 523.连续的子数组和.py
"""
#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#

# @lc code=start
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            rem = prefix % k
            if rem in dic:
                if dic[rem] <= i - 2:
                    return True
            else:
                dic[rem] = i
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.checkSubarraySum([23, 2, 6, 4, 7], 13)
    print(ans)
