#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-08 22:10
FileName: algorithm/P2591. 将钱分给最多的儿童.py
Description:2591. 将钱分给最多的儿童
"""


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1
        ans = min(money // 7, children)
        money -= ans * 7
        children -= ans
        if children == 0 and money or children == 1 and money == 3:
            ans -= 1
        return ans


if __name__ == '__main__':
    print(Solution().distMoney(money=20, children=3))
