#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-24 22:20
FileName: algorithm
Description:P2843. 统计对称整数的数目.py 
"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def check(num):
            even, odd, n = 0, 0, len(str(num))
            for i in range(n // 2):
                even += ord(str(num)[i]) - ord('0')
                odd += ord(str(num)[n // 2 + i]) - ord('0')
            return even == odd

        cnt = 0
        for num in range(low, high + 1):
            if len(str(num)) % 2 == 0 and check(num):
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().countSymmetricIntegers(1200, 1230))
