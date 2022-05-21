#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-21 22:40:08
LastEditTime: 2022-05-21 22:40:09
Description: 
FilePath: 剑指 Offer II 049. 从根节点到叶节点的路径数字之和.py
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, preSum):
            if not root:
                return 0
            sum_ = preSum * 10 + root.val
            if not root.left and not root.right:
                return sum_
            return dfs(root.left, sum_) + dfs(root.right, sum_)

        return dfs(root, 0)
