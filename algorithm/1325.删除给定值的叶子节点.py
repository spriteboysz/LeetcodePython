#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 16:13:20
LastEditTime: 2022-04-05 16:16:21
Description: 
FilePath: 1325.删除给定值的叶子节点.py
"""
#
# @lc app=leetcode.cn id=1325 lang=python3
#
# [1325] 删除给定值的叶子节点
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
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def dfs(node):
            if node.left and dfs(node.left):
                node.left = None
            if node.right and dfs(node.right):
                node.right = None
            if node.val == target and not node.left and not node.right:
                return True

        if not root:
            return root
        return None if dfs(root) else root


# @lc code=end
