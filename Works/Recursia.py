def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)

def sum_n(n):
    if n <= 0:
        return 0
    return n + sum_n(n - 1)

def power(n, m):
    if m == 1:
        return n
    return n * power(n, m - 1)

def count_dig(n):
    if n <= 0:
        return 0
    return 1 + count_dig(n // 10)

def sum_dig(n):
    if n <= 0:
        return 0
    a = n % 10
    return a + sum_dig(n // 10)

def reverse_num(n, result=0):
    if n <= 0:
        return result
    return reverse_num(n // 10, result * 10 + n % 10)

def fibanachi(n):
    if n <= 1:
        return n
    return fibanachi(n - 1) + fibanachi(n - 2)

def hanoi(n, source, target, spare):
    if n == 0:
        return
    hanoi(n - 1, source, spare, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, spare, target, source)

def subsets(nums, k, start=0, current=[]):
    if len(current) == k:
        print(current)
        return
    for i in range(start, len(nums)):
        subsets(nums, k, i + 1, current + [nums[i]])

def permutations(rest, current=""):
    if rest == "":
        print(current)
        return
    for i in range(len(rest)):
        permutations(rest[:i] + rest[i + 1:], current + rest[i])


maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
]

n = len(maze)
m = len(maze[0])
visited = [[False] * m for _ in range(n)]
path = []

def solve(r, c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return False

    if maze[r][c] == 1 or visited[r][c]:
        return False

    visited[r][c] = True
    path.append((r, c))

    if r == n - 1 and c == m - 1:
        return True

    if solve(r, c + 1) or solve(r + 1, c) or solve(r, c - 1) or solve(r - 1, c):
        return True

    path.pop()
    return False

if solve(0, 0):
    print("Путь:")
    print(" -> ".join(str(p) for p in path))

    grid = [[str(x) for x in row] for row in maze]

    for r, c in path:
        grid[r][c] = "*"

    print("\nЛабиринт с путём:")

    for row in grid:
        print(" ".join(row))
else:
    print("Пути нет")


N = 4

board = []

for i in range(N):
    board.append(["."] * N)

def is_safe(row, col):
    for i in range(row):
        if board[i][col] == "Q":
            return False

    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solve(row):
    if row == N:
        print("Solution:")

        for line in board:
            print(" ".join(line))

        print()
        return

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = "Q"

            solve(row + 1)

            board[row][col] = "."

solve(0)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

print("Preorder: ", end="")
preorder(root)
print()

print("Inorder:  ", end="")
inorder(root)
print()

print("Postorder:", end=" ")
postorder(root)
print()