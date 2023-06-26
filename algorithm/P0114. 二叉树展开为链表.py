#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 23:24:18
LastEditTime: 2022-03-30 23:29:12
Description: 
FilePath: 114.二叉树展开为链表.py
"""
from common.TreeNode import TreeNode


#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node:
                return
            nodes.append(node)
            dfs(node.left)
            dfs(node.right)

        nodes = []
        dfs(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

# @lc code=end
