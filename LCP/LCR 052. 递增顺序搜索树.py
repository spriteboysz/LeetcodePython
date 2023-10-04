#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 16:44
FileName: LCP
Description:LCR 052. 递增顺序搜索树.py 
"""
from common.TreeNode import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)

        nodes = []
        dfs(root)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]


if __name__ == '__main__':
    print(Solution().increasingBST(TreeNode.create("[5,3,6,2,4,null,8,1,null,null,null,7,9]")))
