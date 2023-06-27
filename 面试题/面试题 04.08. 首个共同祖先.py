#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-11 16:21
LastEditTime: 2022-06-11 16:21
Description:
FilePath: 面试题 04.08. 首个共同祖先.py
"""


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
            self,
            root: TreeNode,
            p: TreeNode,
            q: TreeNode) -> TreeNode:
        def dfs(node, p, q):
            if not node:
                return
            elif node == p or node == q:
                return node
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right

        return dfs(root, p, q)
