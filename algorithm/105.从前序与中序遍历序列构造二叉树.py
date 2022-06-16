#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-16 22:52
LastEditTime: 2022-06-16 22:52
Description: 
FilePath: 105.从前序与中序遍历序列构造二叉树.py
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return
        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])

        return root