#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 23:00:41
LastEditTime: 2022-04-13 23:09:29
Description:
FilePath: 99.恢复二叉搜索树.py
"""

from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes1.append(node)
            dfs(node.right)

        nodes1 = []
        dfs(root)
        nodes2 = sorted(nodes1, key=lambda node: node.val)
        for node1, node2 in zip(nodes1, nodes2):
            if node1.val != node2.val:
                node1.val, node2.val = node2.val, node1.val
                return
        print(root)


if __name__ == '__main__':
    root = TreeNode.create('[1,3,null,null,2]')
    Solution().recoverTree(root)
