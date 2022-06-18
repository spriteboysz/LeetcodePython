#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-18 22:37
LastEditTime: 2022-06-18 22:37
Description: 
FilePath: 剑指 Offer II 054. 所有大于等于节点的值之和.py
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            nonlocal sums
            if not node:
                return
            dfs(node.right)
            sums += node.val
            node.val = sums
            dfs(node.left)
            return node

        sums = 0
        dfs(root)
        return root