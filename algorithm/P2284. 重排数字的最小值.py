#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-08 21:52:40
LastEditTime: 2022-02-08 22:02:06
Description:
FilePath: 2284.重排数字的最小值.py
"""
#
# @lc app=leetcode.cn id=2284 lang=python3
#
# [2165] 重排数字的最小值
#

# @lc code=start


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            numbers = sorted(map(int, str(num)))
            position = numbers.count(0)
            numbers = numbers[position:position+1] + \
                numbers[:position] + numbers[position+1:]
            smallest = 0
            for number in numbers:
                smallest = smallest * 10 + number
            return smallest
        elif num < 0:
            numbers = sorted(map(int, str(abs(num))), reverse=True)
            smallest = 0
            for number in numbers:
                smallest = smallest * 10 + number
            return -smallest
        else:
            return 0
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.smallestNumber(310))
    print(s.smallestNumber(-7605))
