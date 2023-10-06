#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 00:07
FileName: LCP
Description:LCR 177. 撞色搭配.py 
"""
from collections import defaultdict
from typing import List


class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        dic = defaultdict(int)
        for socket in sockets:
            dic[socket] += 1
        single = []
        for k, v in dic.items():
            if v == 1:
                single.append(k)
        return single


if __name__ == '__main__':
    print(Solution().sockCollocation(sockets=[4, 5, 2, 4, 6, 6]))
