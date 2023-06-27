#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 22:41:57
LastEditTime: 2022-03-30 22:42:26
Description: 
FilePath: 617.合并二叉树.py
"""


#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 or not root2:
            return root1 or root2
        root1.val = root1.val + root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

# @lc code=end
