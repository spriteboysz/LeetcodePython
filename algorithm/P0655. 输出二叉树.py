#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-18 20:15
FileName: algorithm
Description:P0655. 输出二叉树.py 
"""
from collections import deque
from typing import Optional, List

from common.TreeNode import TreeNode


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height, queue = -1, [root]
        while queue:
            height += 1
            nodes = queue
            queue = []
            for node in nodes:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        print(height)
        m = height + 1
        n = 2 ** m - 1
        levels = [[''] * n for _ in range(m)]
        queue = deque([(root, 0, (n - 1) // 2)])
        while queue:
            node, r, c = queue.popleft()
            levels[r][c] = str(node.val)
            if node.left:
                queue.append((node.left, r + 1, c - 2 ** (height - r - 1)))
            if node.right:
                queue.append((node.right, r + 1, c + 2 ** (height - r - 1)))
        return levels


if __name__ == '__main__':
    root = TreeNode.create("[1,2,3,null,4]")
    print(Solution().printTree(root))
