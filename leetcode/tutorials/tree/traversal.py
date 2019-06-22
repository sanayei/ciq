# Binary Tree Preorder Traversal

#Given a binary tree, return the preorder traversal of its nodes' values.

# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,2,3]

# Follow up: Recursive solution is trivial, could you do it iteratively?



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    list_nodes = []

    def _helper(node):
        if node is None:
            return
        else:
            list_nodes.append(node.val)
            _helper(node.left)
            _helper(node.right)

    _helper(root)
    return list_nodes

def preorderTraversal_iterative(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    list_nodes = []
    stack = []
    if root is not None:
        stack.append(root)
    while stack:
        node = stack.pop()
        if node is not None:
            list_nodes.append(node.val)
            # note that we first add right branch then left. because we are using stack, we add first the one that we use last
            stack.append(node.right)
            stack.append(node.left)

    return list_nodes



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



# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?


def postorderTraversal(root):
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
            _helper(node.right)
            list_nodes.append(node.val)

    _helper(root)
    return list_nodes
