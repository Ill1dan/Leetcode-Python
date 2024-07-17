class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delNodes(root, to_delete):
    store = {}

    def dfs(root):
        if root is None:
            return

        left = None
        right = None

        if root.left:
            left = root.left
            if left.val in to_delete:
                root.left = None
                dfs(left)

        if root.right:
            right = root.right
            if right.val in to_delete:
                root.right = None
                dfs(right)

        store[root.val] = [left, right]


        dfs(root.left)
        dfs(root.right)

    dfs(root)
    output = []

    if root.val not in to_delete:
        output.append(root)

    for x in to_delete:
        if store[x][0] and store[x][0].val not in to_delete:
            output.append(store[x][0])
        if store[x][1] and store[x][1].val not in to_delete:
            output.append(store[x][1])

    return output


root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

to_delete = [2, 3]

print(delNodes(root, to_delete))