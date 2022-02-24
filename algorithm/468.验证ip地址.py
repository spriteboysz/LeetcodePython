#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-24 23:41:07
LastEditTime: 2022-02-24 23:42:42
Description: 
FilePath: 468.验证ip地址.py
"""
#
# @lc app=leetcode.cn id=468 lang=python3
#
# [468] 验证IP地址
#

# @lc code=start
from string import hexdigits


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            ip = queryIP.split(".")
            if len(ip) != 4:
                return "Neither"
            for item in ip:
                if (len(item) > 1 and item.startswith("0")) or not item.isdigit():
                    return "Neither"
                if int(item) < 0 or int(item) > 255:
                    return "Neither"
            return "IPv4"
        elif ":" in queryIP:
            ip = queryIP.split(":")
            if len(ip) != 8:
                return "Neither"
            for item in ip:
                if len(item) < 1 or len(item) > 4:
                    return "Neither"
                for el in item:
                    if el not in hexdigits:
                        return "Neither"
            return "IPv6"
        else:
            return "Neither"


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.validIPAddress("192.0.0.1")
    print(ans)
    ans2 = solution.validIPAddress("256.@1.0.1")
    print(ans2)
    ans3 = solution.validIPAddress("ABC:1:1:1:1:1:1:1")
    print(ans3)
