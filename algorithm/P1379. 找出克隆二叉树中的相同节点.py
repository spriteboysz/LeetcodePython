#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 14:21:37
LastEditTime: 2022-03-19 14:24:32
Description: 
FilePath: 1379.找出克隆二叉树中的相同节点.py
"""


#
# @lc app=leetcode.cn id=1379 lang=python3
#
# [1379] 找出克隆二叉树中的相同节点
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
            self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:

        self.targetcopy = TreeNode()

        def dfs(node):
            # nonlocal targetcopy
            if not node:
                return
            if node.val == target.val:
                self.targetcopy = node
                return
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(cloned)
        return self.targetcopy

# @lc code=end
