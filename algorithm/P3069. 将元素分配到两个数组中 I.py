#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 12:26
FileName: algorithm
Description:P3069. 将元素分配到两个数组中 I.py 
"""
from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        for num in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
        return arr1 + arr2


if __name__ == '__main__':
    print(Solution().resultArray(nums=[5, 4, 3, 8]))
