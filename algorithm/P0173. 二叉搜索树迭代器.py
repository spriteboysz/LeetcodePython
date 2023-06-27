#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 20:55:08
LastEditTime: 2022-04-09 22:00:18
Description: 
FilePath: 173.二叉搜索树迭代器.py
"""
#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.queue = deque([])

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.queue.append(node.val)
            dfs(node.right)

        dfs(root)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return True if self.queue else False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
