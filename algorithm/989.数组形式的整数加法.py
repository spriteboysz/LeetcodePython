#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-19 23:30:35
LastEditTime: 2022-01-19 23:45:59
Description: 
FilePath: 989.数组形式的整数加法.py
'''
#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        b = list(map(int, list(str(k))))
        if len(num) < len(b):
            num, b = b, num
        b = [0] * (len(num) - len(b)) + b
        carry = 0
        for i in range(len(num) - 1, -1, -1):
            num[i] += b[i] + carry
            carry, num[i] = divmod(num[i], 10)
        return [carry] + num if carry == 1 else num


# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.addToArrayForm([2, 7, 4], 181))
