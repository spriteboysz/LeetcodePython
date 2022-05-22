#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 17:45
LastEditTime: 2022-05-22 17:45
Description:
FilePath: 面试题 04.05. 合法二叉搜索树.py
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)
        return sorted(set(values)) == values
