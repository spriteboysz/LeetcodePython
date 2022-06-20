#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-20 23:00
LastEditTime: 2022-06-20 23:00
Description:
FilePath: 剑指 Offer II 055. 二叉搜索树迭代器.py
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.values.append(node.val)
            dfs(node.right)

        self.values = []
        dfs(root)

    def next(self) -> int:
        return self.values.pop(0)

    def hasNext(self) -> bool:
        return bool(self.values)
