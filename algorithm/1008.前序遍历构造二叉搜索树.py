#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 23:15:06
LastEditTime: 2022-04-05 23:18:09
Description: 
FilePath: 1008.前序遍历构造二叉搜索树.py
"""
#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 前序遍历构造二叉搜索树
#

# @lc code=start
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def maketree(preorder):
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            elif len(preorder) == 0:
                return None
            node = TreeNode(preorder[0])
            node.left = maketree([i for i in preorder if i < preorder[0]])
            node.right = maketree([i for i in preorder if i > preorder[0]])
            return node

        root = maketree(preorder)
        return root


# @lc code=end
