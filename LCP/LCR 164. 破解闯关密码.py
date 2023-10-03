#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:57
FileName: LCP
Description:LCR 164. 破解闯关密码.py 
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def crackPassword(self, password: List[int]) -> str:
        return ''.join(sorted(map(str, password), key=cmp_to_key(lambda x, y: -(x + y <= y + x))))


if __name__ == '__main__':
    print(Solution().crackPassword(password=[0, 3, 30, 34, 5, 9]))
