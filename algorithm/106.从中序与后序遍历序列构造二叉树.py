#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-16 23:00
LastEditTime: 2022-06-16 23:00
Description: 
FilePath: 106.从中序与后序遍历序列构造二叉树.py
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i + 1:], postorder[i:-1])

        return root

