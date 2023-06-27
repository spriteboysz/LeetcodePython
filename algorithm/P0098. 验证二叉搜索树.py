#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 23:15:21
LastEditTime: 2022-03-30 23:17:18
Description: 
FilePath: 98.验证二叉搜索树.py
"""
from common.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)
        # print(self.values)
        for i in range(len(values) - 1):
            if values[i] >= values[i + 1]:
                return False
        return True
