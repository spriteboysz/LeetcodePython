#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-18 16:31
FileName: algorithm
Description:P1529. 最少的后缀翻转次数.py 
"""


class Solution:
    def minFlips(self, target: str) -> int:
        target = target.lstrip('0')
        if not target:
            return 0
        while '00' in target:
            target = target.replace('00', '0')
        while '11' in target:
            target = target.replace('11', '1')
        return len(target)


if __name__ == '__main__':
    print(Solution().minFlips(target="11000"))
