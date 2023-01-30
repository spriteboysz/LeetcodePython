#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/29 22:17
FileName: algorithm/P2455. 可被三整除的偶数的平均值.py
Description: 
"""
from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total, cnt = 0, 0
        for num in nums:
            if num % 6 == 0:
                total += num
                cnt += 1
        return 0 if cnt == 0 else total // cnt


if __name__ == '__main__':
    print(Solution().averageValue(nums=[1, 3, 6, 10, 12, 15]))
