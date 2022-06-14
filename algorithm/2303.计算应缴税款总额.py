#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-14 22:54
LastEditTime: 2022-06-14 22:54
Description:
FilePath: 2303.计算应缴税款总额.py
"""

from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax, lower = 0, 0
        for upper, percent in brackets:
            if income >= upper:
                tax += (upper - lower) * percent / 100
                lower = upper
            else:
                tax += (income - lower) * percent / 100
                break
        return tax


if __name__ == '__main__':
    solution = Solution()
    ans = solution.calculateTax(
        brackets=[[3, 50], [7, 10], [12, 25]], income=10)
    print(ans)
    ans = solution.calculateTax(brackets=[[2, 50]], income=0)
    print(ans)
