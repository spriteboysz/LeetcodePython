#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-20 22:29:02
LastEditTime: 2022-05-20 22:31:29
Description: 
FilePath: 剑指 Offer 55 - I. 二叉树的深度.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
