#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-05-20 22:23:36
LastEditTime: 2022-05-20 22:25:51
Description: 
FilePath: 剑指 Offer 54. 二叉搜索树的第k大节点.py
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        
        values = []
        dfs(root)
        return values[-k]