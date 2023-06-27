#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 21:15:39
LastEditTime: 2022-05-01 21:19:11
Description: 
FilePath: 剑指 Offer 28. 对称的二叉树.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
