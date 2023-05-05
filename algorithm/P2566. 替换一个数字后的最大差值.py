#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-04 23:26
FileName: algorithm/P2566. 替换一个数字后的最大差值.py
Description: 
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        maximum, minimum = str(num), str(num)
        for c in maximum:
            if c != "9":
                maximum = maximum.replace(c, "9")
                break
        minimum = minimum.replace(minimum[0], "0")

        return int(maximum) - int(minimum)


if __name__ == '__main__':
    print(Solution().minMaxDifference(num=11891))
