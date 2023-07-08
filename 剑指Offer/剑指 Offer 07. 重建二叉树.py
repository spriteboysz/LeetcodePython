#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-18 23:07
LastEditTime: 2022-06-18 23:07
Description:
FilePath: 剑指 Offer 07. 重建二叉树.py
"""

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode | None:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: index + 1], inorder[0: index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root
