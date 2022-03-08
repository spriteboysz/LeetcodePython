#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-08 23:04:59
LastEditTime: 2022-03-08 23:07:58
Description: 
FilePath: 700.二叉搜索树中的搜索.py
"""
#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val > val:
                return self.searchBST(root.left, val)
            elif root.val < val:
                return self.searchBST(root.right, val)
        return root


# @lc code=end
