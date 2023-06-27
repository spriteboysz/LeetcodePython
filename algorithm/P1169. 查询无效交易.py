#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-04 22:24:44
LastEditTime: 2022-03-04 22:32:34
Description: 
FilePath: 1169.查询无效交易.py
"""
#
# @lc app=leetcode.cn id=1169 lang=python3
#
# [1169] 查询无效交易
#

# @lc code=start
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            if int(amount) > 1000:
                invalid.append(transaction)
                continue
            for j, transaction2 in enumerate(transactions):
                if i != j:
                    name2, time2, _, city2 = transaction2.split(",")
                    if (
                            name == name2
                            and city != city2
                            and abs(int(time) - int(time2)) <= 60
                    ):
                        invalid.append(transaction)
                        break
        return invalid


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.invalidTransactions(["alice,20,800,mtv", "alice,50,100,beijing"])
    print(ans)
    ans = solution.invalidTransactions(["alice,20,800,mtv", "alice,50,1200,mtv"])
    print(ans)
    ans = solution.invalidTransactions(["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"])
    print(ans)
