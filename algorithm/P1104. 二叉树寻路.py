#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-15 22:15
FileName: algorithm
Description:P1104. 二叉树寻路.py 
"""
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = [label]
        while label != 1:
            ss = bin(label)[2:-1]
            ss = ss[0] + "".join([str(1 - int(c)) for c in ss[1:]])
            label = int(ss, 2)
            path.append(label)
        return list(reversed(path))


if __name__ == '__main__':
    print(Solution().pathInZigZagTree(14))
