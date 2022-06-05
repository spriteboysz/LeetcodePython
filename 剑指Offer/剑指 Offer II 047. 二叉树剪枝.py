#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 18:02
LastEditTime: 2022-06-05 18:02
Description:
FilePath: 剑指 Offer II 047. 二叉树剪枝.py
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return True
            left0, right0 = dfs(node.left), dfs(node.right)
            if left0 and right0 and node.val == 0:
                return True
            if left0:
                node.left = None
            if right0:
                node.right = None
            return False

        return None if dfs(root) else root
