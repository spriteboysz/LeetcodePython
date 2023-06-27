#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-11 22:56:41
LastEditTime: 2022-04-11 23:00:12
Description: 
FilePath: 235.二叉搜索树的最近公共祖先.py
"""


#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
            self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node):
            if node.val < min(p.val, q.val):
                return dfs(node.right)
            elif node.val > max(p.val, q.val):
                return dfs(node.left)
            else:
                return node

        return dfs(root)

# @lc code=end
