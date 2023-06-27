#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 20:55:14
LastEditTime: 2022-04-05 20:55:48
Description: 
FilePath: 543.二叉树的直径.py
"""


#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 1

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right + 1)
            return max(left, right) + 1

        dfs(root)
        return diameter - 1

# @lc code=end
