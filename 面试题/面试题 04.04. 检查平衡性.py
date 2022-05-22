#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 17:39
LastEditTime: 2022-05-22 17:39
Description:
FilePath: 面试题 04.04. 检查平衡性.py
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1

        if not root:
            return True
        if abs(depth(root.left) - depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
