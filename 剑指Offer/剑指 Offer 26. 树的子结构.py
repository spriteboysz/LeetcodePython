#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 11:29
LastEditTime: 2022-06-19 11:29
Description:
FilePath: 剑指 Offer 26. 树的子结构.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (
                recur(A, B)
                or self.isSubStructure(A.left, B)
                or self.isSubStructure(A.right, B)
        )
