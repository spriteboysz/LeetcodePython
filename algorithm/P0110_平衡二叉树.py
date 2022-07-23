#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-28 23:25:56
LastEditTime: 2022-03-28 23:28:54
Description: 
FilePath: 110.平衡二叉树.py
"""
#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node, depth):
            if not node:
                return 0
            l = dfs(node.left, depth + 1)
            r = dfs(node.right, depth + 1)
            return max(l, r) + 1

        if not root:
            return True
        if abs(dfs(root.left, 0) - dfs(root.right, 0)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


# @lc code=end
