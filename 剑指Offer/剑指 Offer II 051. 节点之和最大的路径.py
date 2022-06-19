#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 23:14
LastEditTime: 2022-06-19 23:14
Description:
FilePath: 剑指 Offer II 051. 节点之和最大的路径.py
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.sums = max(self.sums, left + right + node.val)
            return max(0, node.val, node.val + left, node.val + right)



        self.sums = root.val
        dfs(root)
        return self.sums
