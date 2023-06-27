#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-27 23:05:28
LastEditTime: 2022-03-27 23:07:24
Description: 
FilePath: 222.完全二叉树的节点个数.py
"""
from common.TreeNode import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal count
            if not node:
                return
            count += 1
            dfs(node.left)
            dfs(node.right)

        count = 0
        dfs(root)
        return count
