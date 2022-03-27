#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-27 23:05:28
LastEditTime: 2022-03-27 23:07:24
Description: 
FilePath: 222.完全二叉树的节点个数.py
"""
#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
from platform import node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            self.count += 1
            dfs(node.left)
            dfs(node.right)

        self.count = 0
        dfs(root)
        return self.count


# @lc code=end
