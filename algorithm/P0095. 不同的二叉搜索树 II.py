#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-01 22:19
FileName: algorithm
Description:P0095. 不同的二叉搜索树 II.py 
"""
from typing import List, Optional

from common.TreeNode import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        roots = [[[None] for _ in range(n + 2)] for _ in range(n + 2)]
        for index in range(1, n + 1):
            for i in range(1, n + 2 - index):
                j = i + index - 1
                roots[i][j] = []
                k: int
                for k in range(i, j + 1):
                    for left in roots[i][k - 1]:
                        for right in roots[k + 1][j]:
                            roots[i][j].append(TreeNode(k, left, right))
        return roots[1][n]


if __name__ == '__main__':
    print(Solution().generateTrees(3))
    for root in Solution().generateTrees(3):
        print(root)
