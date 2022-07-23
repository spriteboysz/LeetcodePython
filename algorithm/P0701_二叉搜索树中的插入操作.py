#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-06 22:55:16
LastEditTime: 2022-04-06 22:58:40
Description: 
FilePath: 701.二叉搜索树中的插入操作.py
"""
#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


# @lc code=end
