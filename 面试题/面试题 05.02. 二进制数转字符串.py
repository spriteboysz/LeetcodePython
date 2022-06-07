#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-07 23:58
LastEditTime: 2022-06-07 23:58
Description: 
FilePath: 面试题 05.02. 二进制数转字符串.py
"""

class Solution:
    def printBin(self, num: float) -> str:
        s = ["0", "."]
        while num:
            num *= 2
            if num >= 1:
                s.append("1")
                num -= 1
            else:
                s.append("0")
            if len(s) >= 32 and num:
                return "ERROR"
        return "".join(s)

if __name__ == '__main__':
    solution = Solution()
    ans = solution.printBin(0.625)
    print(ans)
