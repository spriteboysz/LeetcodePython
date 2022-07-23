#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-24 23:33:10
LastEditTime: 2022-04-24 23:42:16
Description: 
FilePath: 2241.设计一个-atm-机器.py
"""
#
# @lc app=leetcode.cn id=2241 lang=python3
#
# [2241] 设计一个 ATM 机器
#

# @lc code=start
from typing import List


class ATM:
    def __init__(self):
        self.value = [20, 50, 100, 200, 500]
        self.balance = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.balance[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        count = [0] * 5
        for i in range(4, -1, -1):
            if amount // self.value[i] and self.balance[i] > 0:
                count[i], amount = divmod(amount, self.value[i])
                self.balance[i] -= count[i]
            if amount == 0:
                print(self.balance)
                return count
        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
# @lc code=end
