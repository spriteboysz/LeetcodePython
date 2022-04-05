#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 23:01:02
LastEditTime: 2022-04-05 23:02:16
Description: 
FilePath: 998.最大二叉树-ii.py
"""
#
# @lc app=leetcode.cn id=998 lang=python3
#
# [998] 最大二叉树 II
#

# @lc code=start
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        values.append(val)
        print(values)

        def maketree(values):
            if not values:
                return
            value = max(values)
            index = values.index(value)
            node = TreeNode(value)
            node.left = maketree(values[:index])
            node.right = maketree(values[index + 1 :])
            return node

        root = maketree(values)
        return root


# @lc code=end
