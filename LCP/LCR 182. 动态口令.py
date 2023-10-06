#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 00:00
FileName: LCP
Description:LCR 182. 动态口令.py 
"""


class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        return password[target:] + password[:target]


if __name__ == '__main__':
    print(Solution().dynamicPassword(password="s3cur1tyC0d3", target=4))
