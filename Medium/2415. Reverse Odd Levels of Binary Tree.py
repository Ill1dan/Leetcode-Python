class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def reverseOddLevels(self, root):
        if not root:
            return None

        # Helper function to perform BFS and reverse odd levels
        def bfs_and_reverse(node):
            queue = [node]
            level = 0

            while queue:
                level_size = len(queue)
                current_level = []
                next_queue = []

                for i in range(level_size):
                    current_node = queue[i]
                    current_level.append(current_node)
                    if current_node.left and current_node.right:
                        next_queue.append(current_node.left)
                        next_queue.append(current_node.right)

                # Reverse node values at odd levels
                if level % 2 == 1:
                    start, end = 0, len(current_level) - 1
                    while start < end:
                        current_level[start].val, current_level[end].val = current_level[end].val, current_level[start].val
                        start += 1
                        end -= 1

                queue = next_queue
                level += 1

        bfs_and_reverse(root)
        return root