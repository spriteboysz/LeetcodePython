#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 00:05:09
LastEditTime: 2022-04-09 00:12:50
Description: 
FilePath: 993.二叉树的堂兄弟节点.py
"""
#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        result_x, result_y = [], []

        def dfs(node, parent, deep):
            if not node:
                return
            nonlocal result_x, result_y
            if node.val == x:
                result_x = [parent, deep]
            elif node.val == y:
                result_y = [parent, deep]
            dfs(node.left, node, deep + 1)
            dfs(node.right, node, deep + 1)

        dfs(root, root, 0)
        return result_x[0] != result_y[0] and result_x[1] == result_y[1]


# @lc code=end
