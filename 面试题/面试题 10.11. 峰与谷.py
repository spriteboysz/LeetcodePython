#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-10 22:54
LastEditTime: 2022-06-10 22:54
Description:
FilePath: 面试题 10.11. 峰与谷.py
"""

from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(0, len(nums), 2):
            if i <= len(nums) - 2:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

if __name__ == '__main__':
    solution = Solution()
    ans = solution.wiggleSort([5, 3, 1, 2, 3])
    print(ans)
