#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-26 22:43
FileName: algorithm
Description:P3192. 使二进制数组全部等于 1 的最少操作次数 II.py 
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i, num in enumerate(nums):
            if cnt % 2:
                nums[i] = 1 - num
            # 如果是0，则需要反转
            if nums[i] == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().minOperations(nums=[0, 1, 1, 0, 1]))
