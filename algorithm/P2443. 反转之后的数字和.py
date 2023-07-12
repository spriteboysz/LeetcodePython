#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-11 23:27
FileName: algorithm/P2443. 反转之后的数字和.py
Description: 
"""


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num + 1):
            rev = int("".join(list(reversed(str(i)))))
            if i + rev == num:
                return True
        return False


if __name__ == '__main__':
    print(Solution().sumOfNumberAndReverse(443))
