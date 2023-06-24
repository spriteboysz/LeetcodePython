#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 21:56
FileName: algorithm/P2739. 总行驶距离.py
Description: 
"""


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10


if __name__ == '__main__':
    print(Solution().distanceTraveled(5, 10))
