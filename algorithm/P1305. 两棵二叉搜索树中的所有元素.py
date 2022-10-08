#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-03 21:53:42
LastEditTime: 2022-04-03 22:01:30
Description: 
FilePath: 1305.两棵二叉搜索树中的所有元素.py
"""
#
# @lc app=leetcode.cn id=1305 lang=python3
#
# [1305] 两棵二叉搜索树中的所有元素
#

# @lc code=start
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, value):
            if not node:
                return
            dfs(node.right, value)
            value.append(node.val)
            dfs(node.left, value)

        stack1, stack2, values = [], [], []
        dfs(root1, stack1)
        dfs(root2, stack2)
        # print(stack1, stack2)
        while stack1 or stack2:
            if not stack1:
                values.extend(stack2[::-1])
                break
            elif not stack2:
                values.extend(stack1[::-1])
                break
            else:
                if stack1[-1] <= stack2[-1]:
                    values.append(stack1.pop())
                else:
                    values.append(stack2.pop())
        return values


# @lc code=end
