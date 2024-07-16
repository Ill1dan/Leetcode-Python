class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getDirections(root, startValue, destValue):
        store = {}

        def dfs(root, parent=0):
            if root is None:
                return

            left = 0
            right = 0

            if root.left:
                left = root.left.val
            if root.right:
                right = root.right.val
            store[root.val] = [left, right, parent]

            dfs(root.left, root.val)
            dfs(root.right, root.val)

        dfs(root)

        route1 = []
        route2 = []

        parent = startValue
        while parent != 0:
            route1.append(parent)
            parent = store[parent][2]

        parent = destValue
        while parent != 0:
            route2.append(parent)
            parent = store[parent][2]

        route = []
        end = 0

        for i in route1:
            route.append(i)

        for j in route2[::-1]:
            if route and j == route[-1]:
                route.pop(-1)
                route2.pop(-1)
                end = j

        if end:
            route.append(end)

        for k in route2[::-1]:
            route.append(k)

        output = ""
        current = startValue
        for x in range(len(route) - 1):
            if route[x + 1] == store[current][0]:
                output += "L"
            elif route[x + 1] == store[current][1]:
                output += "R"
            elif route[x + 1] == store[current][2]:
                output += "U"
            current = route[x + 1]

        print(" --> ".join((str(x) for x in route)))

        return output


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)
startValue = 3
destValue = 6

print(getDirections(root, startValue, destValue))