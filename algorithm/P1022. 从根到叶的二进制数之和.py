#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-29 23:56:27
LastEditTime: 2022-03-30 00:00:16
Description: 
FilePath: 1022.从根到叶的二进制数之和.py
"""

from collections import deque
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        paths, queue = [], deque()
        queue.append((root, str(root.val)))
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                queue.append((node.left, path + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + str(node.right.val)))
        print(paths)
        return sum(map(lambda el: int(el, 2), paths))


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumRootToLeaf(TreeNode.create("[1,0,1,0,1,0,1]")))
