#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-13 22:50
LastEditTime: 2022-06-13 22:50
Description:
FilePath: 866.回文素数.py
"""


class Solution:
    def primePalindrome(self, n: int) -> int:
        def prime(n):
            return n >= 2 and all(n % i for i in range(2, int(n ** 0.5) + 1))

        if 8 <= n <= 11:
            return 11
        length = len(str(n))
        h = int(str(n)[:(length + 1) // 2])
        for half in range(h, 10 ** 6):
            num = int(str(half) + str(half)[-2::-1])
            if num >= n and prime(num):
                return num


if __name__ == '__main__':
    solution = Solution()
    ans = solution.primePalindrome(6)
    print(ans)
