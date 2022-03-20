#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-20 16:27:37
LastEditTime: 2022-03-20 16:28:17
Description: 
FilePath: 2117.一个区间内所有数乘积的缩写.py
"""
#
# @lc app=leetcode.cn id=2117 lang=python3
#
# [2117] 一个区间内所有数乘积的缩写
#

# @lc code=start
from math import factorial


class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        product = str(factorial(right) // factorial(left - 1))
        # <pre>...<suf>e<c>
        c = str(len(product) - len(product.rstrip("0")))
        if len(product := product.rstrip("0")) <= 10:
            return product + "e" + c
        else:
            return product[:5] + "..." + product[-5:] + "e" + c


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.abbreviateProduct(2, 11)
    print(ans)
