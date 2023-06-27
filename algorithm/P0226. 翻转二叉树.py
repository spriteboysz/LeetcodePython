#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-27 23:10:19
LastEditTime: 2022-03-27 23:12:51
Description: 
FilePath: 226.翻转二叉树.py
"""


#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# @lc code=end
