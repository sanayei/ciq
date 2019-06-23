# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    list_nodes = []

    def _helper(node):
        if node is None:
            return
        else:
            _helper(node.left)
            list_nodes.append(node.val)
            _helper(node.right)

    _helper(root)
    return list_nodes
