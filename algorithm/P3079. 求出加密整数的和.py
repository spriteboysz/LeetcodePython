#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 13:10
FileName: algorithm
Description:P3079. 求出加密整数的和.py 
"""
from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(num):
            ss = list(str(num))
            return int(max(ss)) * int('1' * len(ss))

        return sum(map(encrypt, nums))


if __name__ == '__main__':
    print(Solution().sumOfEncryptedInt(nums=[10, 21, 31]))
