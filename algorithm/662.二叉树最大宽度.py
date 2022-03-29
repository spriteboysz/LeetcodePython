#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-28 23:52:07
LastEditTime: 2022-03-29 00:13:44
Description: 
FilePath: 662.二叉树最大宽度.py
"""
#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#

# @lc code=start
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []

        level, queue = [], deque()
        queue.append(root)
        while queue:
            curlevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    curlevel.append(node.val)
                else:
                    curlevel.append("null")
                    continue
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
            level.append(curlevel)

        for i, item in enumerate(level):
            while item and item[0] == "null":
                level[i].pop(0)
            while item and item[-1] == "null":
                level[i].pop()
        return len(max(level, key=len))


# @lc code=end
