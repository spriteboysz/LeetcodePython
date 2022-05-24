#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-23 23:44
LastEditTime: 2022-05-23 23:44
Description:
FilePath: 剑指 Offer 68 - II. 二叉树的最近公共祖先.py
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
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left and not right:
            return left
        elif not left and right:
            return right
        else:
            return
