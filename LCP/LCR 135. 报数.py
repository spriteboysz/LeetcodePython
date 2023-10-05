#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:08
FileName: LCP
Description:LCR 135. 报数.py 
"""
from typing import List


class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        return [i for i in range(1, pow(10, cnt))]


if __name__ == '__main__':
    print(Solution().countNumbers(2))
