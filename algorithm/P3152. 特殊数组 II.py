#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-22 21:50
FileName: algorithm
Description:P3152. 特殊数组 II.py 
"""
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        arr = [0]
        for i in range(1, len(nums)):
            if (nums[i - 1] & 1) ^ (nums[i] & 1) == 0:
                arr.append(arr[-1] + 1)
            else:
                arr.append(arr[-1])

        return [arr[left] == arr[right] for left, right in queries]


if __name__ == '__main__':
    print(Solution().isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]))
