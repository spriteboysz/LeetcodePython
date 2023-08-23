#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-22 23:55
FileName: algorithm
Description:P2806. 取整购买后的账户余额.py 
"""


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - (purchaseAmount + 5) // 10 * 10


if __name__ == '__main__':
    print(Solution().accountBalanceAfterPurchase(purchaseAmount=15))
