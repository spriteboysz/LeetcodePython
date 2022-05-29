#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 22:14
LastEditTime: 2022-05-29 22:14
Description:
FilePath: 面试题68 - I. 二叉搜索树的最近公共祖先.py
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
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val < p.val and root.val < q.val:  # p,q 都在 root 的右子树中
                root = root.right
            elif root.val > p.val and root.val > q.val:  # p,q 都在 root 的左子树中
                root = root.left
            else:
                break
        return root
