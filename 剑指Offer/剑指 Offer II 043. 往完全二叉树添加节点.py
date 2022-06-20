#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-20 22:49
LastEditTime: 2022-06-20 22:49
Description:
FilePath: 剑指 Offer II 043. 往完全二叉树添加节点.py
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = deque([self.root])  # 当前层
        self.queue2 = deque([])  # 下一层
        while self.queue:
            a = self.queue[0]
            if not a.left:
                break
            elif not a.right:
                self.queue2.append(a.left)
                break
            else:
                cur = self.queue.popleft()
                self.queue2.append(cur.left)
                self.queue2.append(cur.right)
                if not self.queue:
                    self.queue = self.queue2
                    self.queue2 = deque([])

    def insert(self, v: int) -> int:
        cur = self.queue[0]
        if not cur.left:
            cur.left = TreeNode(v)
            self.queue2.append(cur.left)
        else:
            cur.right = TreeNode(v)
            self.queue2.append(cur.right)
            self.queue.popleft()
            if not self.queue:
                self.queue = self.queue2
                self.queue2 = deque([])
        return cur.val

    def get_root(self) -> TreeNode:
        return self.root
