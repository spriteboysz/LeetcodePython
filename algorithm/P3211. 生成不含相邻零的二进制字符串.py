#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-07-14 18:42
FileName: algorithm
Description:P3211. 生成不含相邻零的二进制字符串.py 
"""
from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        mask = (1 << n) - 1
        for i in range(1 << n):
            x = mask ^ i
            if (x >> 1) & x == 0:
                ans.append(f"{i:0{n}b}")
        return ans


if __name__ == '__main__':
    print(Solution().validStrings(3))
