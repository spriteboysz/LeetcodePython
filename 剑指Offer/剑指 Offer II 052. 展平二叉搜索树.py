#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-21 22:48:53
LastEditTime: 2022-05-21 22:48:54
Description: 
FilePath: 剑指 Offer II 052. 展平二叉搜索树.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        nodes = []
        dfs(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
        nodes[-1].left, nodes[-1].right = None, None

        return nodes[0]
