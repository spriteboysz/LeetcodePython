#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-21 23:08:04
LastEditTime: 2022-05-21 23:08:05
Description: 
FilePath: 剑指 Offer II 056. 二叉搜索树中两个节点之和.py
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)

        for i, num in enumerate(values):
            if k - num in values[:i] + values[i + 1:]:
                return True
        return False
