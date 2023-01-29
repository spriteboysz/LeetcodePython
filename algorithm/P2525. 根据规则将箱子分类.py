#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/29 21:56
FileName: algorithm/P2525. 根据规则将箱子分类.py
Description: 
"""


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 10 ** 9
        heavy = mass >= 100
        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"


if __name__ == '__main__':
    print(Solution().categorizeBox(length=1000, width=35, height=700, mass=300))
