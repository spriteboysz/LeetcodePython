#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-05-15 16:50:28
LastEditTime: 2022-05-15 16:52:32
Description:
FilePath: 剑指 Offer II 002. 二进制加法.py
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
