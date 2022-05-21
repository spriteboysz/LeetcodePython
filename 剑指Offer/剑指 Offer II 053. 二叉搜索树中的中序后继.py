#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-21 23:01:55
LastEditTime: 2022-05-21 23:02:28
Description: 
FilePath: 剑指 Offer II 053. 二叉搜索树中的中序后继.py
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: "TreeNode", p: "TreeNode") -> "TreeNode":
        node = None
        while root:
            if root.val > p.val:
                node = root
                root = root.left
            else:
                root = root.right
        return node
