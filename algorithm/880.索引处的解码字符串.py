#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-15 20:17:58
LastEditTime: 2022-03-15 20:21:50
Description: 
FilePath: 880.索引处的解码字符串.py
"""
#
# @lc app=leetcode.cn id=880 lang=python3
#
# [880] 索引处的解码字符串
#

# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decode, n = "", 0
        for item in s:
            if item.isdigit():
                decode = decode * int(item)
                n = n * int(item)
            else:
                decode += item
                n += 1
            if n >= k:
                break
        return decode[k - 1]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.decodeAtIndex(s="leet2code3", k=10)
    print(ans)
    ans = solution.decodeAtIndex("ha22", 5)
    print(ans)
    ans = solution.decodeAtIndex("a2345678999999999999999", 1)
    print(ans)
