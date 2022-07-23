#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-11 23:09:02
LastEditTime: 2022-04-11 23:18:49
Description: 
FilePath: 572.另一棵树的子树.py
"""
#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return str(subRoot) in str(root)


# @lc code=end
