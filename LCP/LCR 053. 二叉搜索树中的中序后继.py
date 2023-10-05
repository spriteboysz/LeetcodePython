#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 16:50
FileName: LCP
Description:LCR 053. 二叉搜索树中的中序后继.py 
"""
from common.TreeNode import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)

        nodes = []
        dfs(root)
        for i in range(len(nodes) - 1):
            if nodes[i].val == p.val:
                return nodes[i + 1]
        return None


if __name__ == '__main__':
    print(Solution().inorderSuccessor(TreeNode.create("[2,1,3]"), TreeNode(1)))
