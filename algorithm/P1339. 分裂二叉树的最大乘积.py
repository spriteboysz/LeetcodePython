#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-17 22:10
LastEditTime: 2022-06-17 22:10
Description:
FilePath: 1339.分裂二叉树的最大乘积.py
"""

from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def getSum(node):
            nonlocal total
            if not node:
                return
            total += node.val
            getSum(node.left)
            getSum(node.right)

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            curr = node.val + left + right
            nonlocal maximum
            maximum = max(maximum, curr * (total - curr))
            return curr

        total, maximum = 0, -inf
        getSum(root)
        dfs(root)
        return maximum % (10 ** 9 + 7)
