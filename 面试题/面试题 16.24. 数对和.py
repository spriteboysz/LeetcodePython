#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-25 23:48
LastEditTime: 2022-05-25 23:48
Description:
FilePath: 面试题 16.24. 数对和.py
"""

from typing import List

class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        pair, i, j = [], 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                pair.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return pair

if __name__ == '__main__':
    solution = Solution()
    ans = solution.pairSums(nums=[5, 6, 5, 6], target=11)
    print(ans)
