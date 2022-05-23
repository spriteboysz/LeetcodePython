#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 22:29
LastEditTime: 2022-05-22 22:29
Description:
FilePath: 面试题 17.12. BiNode.py
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        if not root:
            return

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
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]
