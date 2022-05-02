#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-02 13:59:37
LastEditTime: 2022-05-02 14:02:49
Description: 
FilePath: 面试题 05.07. 配对交换.py
"""


class Solution:
    def exchangeBits(self, num: int) -> int:
        return ((num & 0xAAAAAAAA) >> 1) | ((num & 0x55555555) << 1)


if __name__ == "__main__":
    solution = Solution()
    ans = solution.exchangeBits(2)
    print(ans)
    ans = solution.exchangeBits(1)
    print(ans)
