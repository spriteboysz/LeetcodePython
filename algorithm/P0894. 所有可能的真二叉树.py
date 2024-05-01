#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-01 20:31
FileName: algorithm
Description:P0894. 所有可能的真二叉树.py 
"""
from functools import cache
from typing import List, Optional

from common.TreeNode import TreeNode


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(n: int) -> List[Optional[TreeNode]]:
            if n == 1:
                return [TreeNode()]
            root = []
            for i in range(n - 1):
                j = n - 1 - i
                for left in dfs(i):
                    for right in dfs(j):
                        root.append(TreeNode(0, left, right))
            return root

        return dfs(n)


if __name__ == '__main__':
    print(Solution().allPossibleFBT(7))
    for root in Solution().allPossibleFBT(7):
        print(root)
