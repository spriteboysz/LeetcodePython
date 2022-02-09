#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-09 22:49:40
LastEditTime: 2022-02-09 22:58:04
Description: 
FilePath: 2043.简易银行系统.py
'''
#
# @lc app=leetcode.cn id=2043 lang=python3
#
# [2043] 简易银行系统
#

# @lc code=start
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.balance) or account2 > len(self.balance):
            return False
        if self.balance[account1 - 1] < money:
            return False
        else:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        if self.balance[account - 1] < money:
            return False
        else:
            self.balance[account - 1] -= money
            return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
# @lc code=end
