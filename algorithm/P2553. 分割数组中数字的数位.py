#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-04 23:44
FileName: algorithm/P2553. 分割数组中数字的数位.py
Description: 
"""
from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list(map(int, list("".join(map(str, nums)))))


if __name__ == '__main__':
    print(Solution().separateDigits(nums=[13, 25, 83, 77]))
