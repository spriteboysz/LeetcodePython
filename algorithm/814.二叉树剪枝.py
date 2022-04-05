#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 16:02:25
LastEditTime: 2022-04-05 16:10:56
Description: 
FilePath: 814.二叉树剪枝.py
"""
#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node.left and dfs(node.left):
                node.left = None
            if node.right and dfs(node.right):
                node.right = None
            if node.val == 0 and not node.left and not node.right:  # 根
                return True

        if not root:
            return root
        return None if dfs(root) else root


# @lc code=end
