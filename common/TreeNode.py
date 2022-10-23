#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 15:31
FileName: common/TreeNode.py
Description: 
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        if not self:
            return ""
        queue = deque([self])
        values = []
        while queue:
            node = queue.popleft()
            if node:
                values.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                values.append('null')
        while values[-1] == "null":
            values.pop()
        return '[' + ','.join(values) + ']'


def create(data=""):
    if not data:
        return []
    values = data[1:-1].split(',')
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] != 'null':
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'null':
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
    return root


if __name__ == '__main__':
    root = "[4,8,5,0,1,null,6]"
    tree = create(root)
    print(tree)
