#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 20:41:42
LastEditTime: 2022-04-05 20:45:16
Description: 
FilePath: 538.把二叉搜索树转换为累加树.py
"""
#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = 0

        def dfs(node):
            nonlocal cur
            if not node:
                return
            dfs(node.right)
            node.val += cur
            cur = node.val
            dfs(node.left)

        dfs(root)
        return root

# @lc code=end
