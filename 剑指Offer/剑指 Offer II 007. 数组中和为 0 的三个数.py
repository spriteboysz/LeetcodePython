#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 15:57
LastEditTime: 2022-06-05 15:57
Description:
FilePath: 剑指 Offer II 007. 数组中和为 0 的三个数.py
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target, left, right = -nums[i], i + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right:
                        left += 1
                        if nums[left - 1] != nums[left]:
                            break
                    while left < right:
                        right -= 1
                        if nums[right + 1] != nums[right]:
                            break
                elif s < target:
                    left += 1
                elif s > target:
                    right -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    ans = solution.threeSum(nums=[-1, 0, 1, 2, -1, -4])
    print(ans)
