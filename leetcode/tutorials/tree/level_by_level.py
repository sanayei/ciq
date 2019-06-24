from collections import deque

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right


def levelOrder_2(root):
    from collections import deque
    cur = deque()
    nxt = deque()
    output = []
    cur.append(root)
    while len(cur) > 0:
        subans = []
        for i in range(len(cur)):
            n = cur.popleft()
            if n is None:
                continue
            subans.append(n.val)
            nxt.append(n.left)
            nxt.append(n.right)
        if len(subans) > 0:
            output.append(subans)
        cur = nxt
    return output

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    from collections import deque
    ans = []
    currentLevel = deque()
    if root is not None:
        currentLevel.append(root)
    while len(currentLevel) > 0:
        subans = []
        nextLevel = deque()
        for i in range(len(currentLevel)):
            n = currentLevel.popleft()
            subans.append(n.val)
            if n.left is not None:
                nextLevel.append(n.left)
            if n.right is not None:
                nextLevel.append(n.right)
        ans.append(subans)
        currentLevel = nextLevel
    return ans

if __name__ == '__main__':
    t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))

    ans = levelOrder(t)
    print(ans)