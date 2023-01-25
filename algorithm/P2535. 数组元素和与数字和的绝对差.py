#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/25 11:46
FileName: algorithm/P2535. 数组元素和与数字和的绝对差.py
Description: 
"""
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum2 = 0
        for num in nums:
            for c in str(num):
                sum2 = sum2 + int(c)
        return sum(nums) - sum2


if __name__ == '__main__':
    print(Solution().differenceOfSum(nums=[1, 15, 6, 3]))
