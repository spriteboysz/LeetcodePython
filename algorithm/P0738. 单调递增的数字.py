#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-12 22:54
FileName: algorithm/P0738. 单调递增的数字.py
Description: 
"""


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        m = len(s)
        for i in range(m - 1, 0, -1):
            if s[i] < s[i - 1]:
                s[i - 1] = str(int(s[i - 1]) - 1)
                s[i:] = ['9'] * (m - i)
        return int(''.join(s))


if __name__ == '__main__':
    print(Solution().monotoneIncreasingDigits(n=332))
    print(Solution().monotoneIncreasingDigits(n=10))
