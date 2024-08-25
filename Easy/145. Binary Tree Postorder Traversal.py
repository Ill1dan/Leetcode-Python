class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    res = []

    def dfs(node):
        if node:
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

    dfs(root)
    return res