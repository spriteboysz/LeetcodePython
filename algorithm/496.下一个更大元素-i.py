#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-01 22:53:00
LastEditTime: 2022-03-01 23:03:07
Description: 
FilePath: 496.下一个更大元素-i.py
"""
#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, stack = {}, []
        for num in nums2:
            while stack and num > stack[-1]:
                dic[stack.pop()] = num
            stack.append(num)

        return [dic.get(num, -1) for num in nums1]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
    print(ans)
    ans = solution.nextGreaterElement([2, 4], [4, 3, 2, 1])
    print(ans)
