#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 18:00
LastEditTime: 2022-05-22 18:00
Description:
FilePath: 面试题 04.10. 检查子树.py
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def dfs(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and dfs(
                t1.left, t2.left) and dfs(
                t1.right, t2.right)

        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if dfs(t1, t2):
            return True
        return self.checkSubTree(
            t1.left, t2) or self.checkSubTree(
            t1.right, t2)
