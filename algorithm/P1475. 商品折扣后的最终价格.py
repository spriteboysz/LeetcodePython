#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-27 23:20:52
LastEditTime: 2022-01-27 23:27:25
Description:
FilePath: 1475.商品折扣后的最终价格.py
"""
#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discount = []
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount.append(prices[i] - prices[j])
                    break
            else:
                discount.append(prices[i])
        discount.append(prices[-1])
        return discount
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.finalPrices([1, 2, 3, 4, 5]))
    print(s.finalPrices([10, 1, 1, 6]))
