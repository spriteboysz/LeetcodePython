#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-12 22:06
FileName: algorithm
Description:P3178. 找出 K 秒后拿着球的孩子.py 
"""


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        m = n + n - 2
        ans = k % m
        return ans if ans < n else m - ans


if __name__ == '__main__':
    print(Solution().numberOfChild(n=3, k=5))
    print(Solution().numberOfChild(n=3, k=6))
