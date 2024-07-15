class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createBinaryTree(descriptions):
    childs = set()
    dict = {}

    for i in descriptions:
        if i[0] not in dict:
            dict[i[0]] = TreeNode(i[0])
        if i[1] not in dict:
            dict[i[1]] = TreeNode(i[1])
        if i[2]:
            dict[i[0]].left = dict[i[1]]
        else:
            dict[i[0]].right = dict[i[1]]

        childs.add(i[1])

    for j in descriptions:
        if j[0] not in childs:
            return dict[j[0]]

    return



descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
print(createBinaryTree(descriptions))