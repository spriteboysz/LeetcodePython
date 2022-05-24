#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-23 23:34
LastEditTime: 2022-05-23 23:34
Description:
FilePath: 剑指 Offer 55 - II. 平衡二叉树.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return 0
            return max(dfs(node.left), dfs(node.right)) + 1

        return abs(dfs(root.left) - dfs(root.right)
                   ) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
