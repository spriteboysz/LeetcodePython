#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-24 23:20
LastEditTime: 2022-05-24 23:20
Description:
FilePath: 面试题 04.03. 特定深度节点链表.py
"""

from typing import List
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        nodes, queue = [], deque([tree])
        while queue:
            head = ListNode(-1)
            cur = head
            for _ in range(len(queue)):
                node = queue.popleft()
                cur.next = ListNode(node.val)
                cur = cur.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            nodes.append(head.next)

        return nodes
