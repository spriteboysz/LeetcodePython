#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 14:04:53
LastEditTime: 2022-03-19 14:05:37
Description: 
FilePath: 1302.层数最深叶子节点的和.py
"""
#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.total, self.maxlevel = 0, 0

        def dfs(node, level):
            if not node:
                return
            if node.left or node.right:
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)
            else:
                if level > self.maxlevel:
                    self.maxlevel = level
                    self.total = node.val
                elif level == self.maxlevel:
                    self.total += node.val

        dfs(root, 0)
        return self.total


# @lc code=end
