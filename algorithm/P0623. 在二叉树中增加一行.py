#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-15 22:20
LastEditTime: 2022-06-15 22:20
Description:
FilePath: 623.在二叉树中增加一行.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if not root:
            return
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        if depth == 2:
            node1, node2 = TreeNode(val), TreeNode(val)
            node1.left, node2.right = root.left, root.right
            root.left, root.right = node1, node2
            return root
        self.addOneRow(root.left, val, depth - 1)
        self.addOneRow(root.right, val, depth - 1)
        return root
