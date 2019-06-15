# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def maxDepth(root: TreeNode) -> int:
    # 1st approach
    def _helper(node, depth):
        if node is None:
            return depth
        return max(_helper(node.left, depth + 1), _helper(node.right, depth + 1))

    # return _helper(root, depth=0)

    # 2nd approach
    def _helper2(node):
        if node is None:
            return 0
        return 1 + max(_helper2(node.left), _helper2(node.right))

    return _helper2(root)