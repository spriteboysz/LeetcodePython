#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-16 22:07:28
LastEditTime: 2022-03-16 22:18:48
Description: 
FilePath: 1864.构成交替字符串需要的最小交换次数.py
"""
#
# @lc app=leetcode.cn id=1864 lang=python3
#
# [1864] 构成交替字符串需要的最小交换次数
#

# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        def xor(a, b):
            return int(a) ^ int(b)

        if abs(s.count("0") - s.count("1")) >= 2:
            return -1
            
        if len(s) % 2 == 0:
            count1 = sum(map(xor, s, "10" * len(s)))
            count2 = sum(map(xor, s, "01" * len(s)))
            return min(count1, count2) // 2
        else:
            target = "01" if s.count("0") > s.count("1") else "10"
            count = sum(map(xor, s, target * len(s)))
            return count // 2


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minSwaps("111000")
    print(ans)
    ans = solution.minSwaps("010")
    print(ans)
    ans = solution.minSwaps("1110")
    print(ans)
