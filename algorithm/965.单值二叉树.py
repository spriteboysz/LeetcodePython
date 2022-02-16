#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 23:12:50
LastEditTime: 2022-02-16 23:15:25
Description: 
FilePath: 965.单值二叉树.py
"""
#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            val = root.val
            if root.left and root.left.val != val:
                return False
            if root.right and root.right.val != val:
                return False
            else:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)


# @lc code=end
