#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-18 22:45:38
LastEditTime: 2022-01-18 23:17:17
Description: 
FilePath: 860.柠檬水找零.py
'''
#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        balance = {5: 0, 10: 0, 20: 0}
        for item in bills:
            balance[item] += 1
            if item == 20:
                if balance[10] >= 1 and balance[5] >= 1:
                    balance[10] -= 1
                    balance[5] -= 1
                elif balance[5] >= 3:
                    balance[5] -= 3
                else:
                    return False
            elif item == 10:
                if balance[5] >= 1:
                    balance[5] -= 1
                else:
                    return False

        return True

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.lemonadeChange([5, 5, 10, 10, 20]))
