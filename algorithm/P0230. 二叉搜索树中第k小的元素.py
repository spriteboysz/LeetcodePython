#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-27 23:16:19
LastEditTime: 2022-03-27 23:21:32
Description: 
FilePath: 230.二叉搜索树中第k小的元素.py
"""

from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)
        return values[k - 1]
