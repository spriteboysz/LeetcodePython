#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-28 23:50:15
LastEditTime: 2022-04-28 23:57:46
Description: 
FilePath: 1357.每隔-n-个顾客打折.py
"""
#
# @lc app=leetcode.cn id=1357 lang=python3
#
# [1357] 每隔 n 个顾客打折
#

# @lc code=start

from typing import List


class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n, self.discount, self.price, self.count = n, discount, {}, 0
        for product, price in zip(products, prices):
            self.price[product] = price

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        bill = sum([self.price[p] * a for p, a in zip(product, amount)])
        if self.count % self.n == 0:
            bill = bill * (100 - self.discount) / 100
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
# @lc code=end
