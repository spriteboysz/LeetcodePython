#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-17 23:45:45
LastEditTime: 2022-02-17 23:51:54
Description: 
FilePath: 238.除自身以外数组的乘积.py
"""
#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        if nums.count(0) >= 2:
            return answer
        else:
            product = 1
            for num in filter(lambda el: el != 0, nums):
                product *= num
            if nums.count(0) == 1:
                answer[nums.index(0)] = product
            else:
                answer = list(map(lambda el: product // el, nums))
            return answer


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.productExceptSelf([-1, 1, 0, -3, 3])
    print(ans)
