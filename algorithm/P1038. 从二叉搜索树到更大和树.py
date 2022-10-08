#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 20:48:00
LastEditTime: 2022-04-05 20:49:58
Description: 
FilePath: 1038.从二叉搜索树到更大和树.py
"""
#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 从二叉搜索树到更大和树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

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
