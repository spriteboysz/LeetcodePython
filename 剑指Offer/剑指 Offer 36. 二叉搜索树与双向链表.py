#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-10 21:54
LastEditTime: 2022-06-10 21:54
Description:
FilePath: 剑指 Offer 36. 二叉搜索树与双向链表.py
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.pre:
                self.pre.right, node.left = node, self.pre
            else:
                self.head = node
            self.pre = node
            dfs(node.right)


        if not root:
            return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
