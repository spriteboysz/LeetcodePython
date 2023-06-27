#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-08 23:29:23
LastEditTime: 2022-03-08 23:30:19
Description: 
FilePath: 872.叶子相似的树.py
"""
#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1, leaf2 = [], []

        def dfs(node, leaf):
            if not node:
                return
            if not node.left and not node.right:
                leaf.append(node.val)
            dfs(node.left, leaf)
            dfs(node.right, leaf)

        dfs(root1, leaf1)
        dfs(root2, leaf2)
        # print(leaf1, leaf2)
        return leaf1 == leaf2

# @lc code=end
