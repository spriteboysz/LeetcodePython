#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-03 22:48:28
LastEditTime: 2022-04-03 22:49:58
Description: 
FilePath: 1367.二叉树中的列表.py
"""
#
# @lc app=leetcode.cn id=1367 lang=python3
#
# [1367] 二叉树中的列表
#

# @lc code=start
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        target = []
        while head:
            target.append(str(head.val))
            head = head.next
        target = "#".join(target)

        queue = deque()
        queue.append((root, str(root.val)))
        while queue:
            node, path = queue.popleft()
            # if not node.left and not node.right:
            if target in path:
                return True
            path += "#"
            if node.left:
                queue.append((node.left, path + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + str(node.right.val)))
        return False

# @lc code=end
