class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def spiralMatrix(self, m, n, head):
        ROWS, COLS = m, n

        matrix = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        visited = set()

        i, j = 0, 0
        current_position = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while head:
            if i < 0 or j < 0 or i == ROWS or j == COLS or (i, j) in visited:
                i -= directions[current_position][0]
                j -= directions[current_position][1]

                current_position = (current_position + 1) % 4

                i += directions[current_position][0]
                j += directions[current_position][1]

            matrix[i][j] = head.val
            visited.add((i, j))

            i += directions[current_position][0]
            j += directions[current_position][1]

            head = head.next

        return matrix


m = 3
n = 5
head = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]