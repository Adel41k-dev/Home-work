#Varianat - 3

#1
def max_sum(arr):
    cur_sum = arr[0]
    max_sume = arr[0]

    for i in range(1, len(arr)):
        cur_sum = max(arr[i], cur_sum + arr[i])
        if cur_sum > max_sume:
            max_sume = cur_sum
    return max_sume

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Task 1")
print(max_sum(arr))

#2
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_l(self, val):
        new_val = Node(val)
        if not self.head:
            self.head = new_val
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_val

    def reverse(self):
        prev = None
        cur = self.head

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        self.head = prev

    def print_linked(self):
        if not self.head:
            print("Empty list")
            return
        cur = self.head
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.next
        print(result)
print("\nTask 2")
list = LinkedList()
list.append_l(1)
list.append_l(2)
list.append_l(3)
list.append_l(4)
list.append_l(5)
list.print_linked()
list.reverse()
list.print_linked()

#3
class Stack:
    def __init__(self):
        self.item = []

    def push(self, val):
        self.item.append(val)

    def pop(self):
        if self.is_empty():
            print("Error")
            return
        self.item.pop()

    def peek(self):
        return self.item[-1]

    def is_empty(self):
        return len(self.item) == 0

    def next_greater(self):
        result = []
        n = len(self.item)
        for i in range(n):
            great = False
            cur = self.item[i]
            for j in range(i + 1, n):
                right = self.item[j]
                if right > cur:
                    result.append(right)
                    great = True
                    break

            if not great:
                result.append(-1)

        print(result)

print("\nTask 3")
stack = Stack()
stack.push(4)
stack.push(5)
stack.push(2)
stack.push(10)
stack.push(8)
stack.next_greater()

#4
class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def _transfer(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def dequeue(self):
        self._transfer()
        if not self.out_stack:
            raise IndexError("dequeue from empty queue")
        print(self.out_stack.pop())


    def peek(self):
        self._transfer()
        if not self.out_stack:
            raise IndexError("peek from empty queue")
        return self.out_stack[-1]

    def is_empty(self):
        return not self.in_stack and not self.out_stack
print("\nTask 4")
queue_stack = QueueUsingStacks()
queue_stack.enqueue(10)
queue_stack.enqueue(20)
queue_stack.enqueue(30)
queue_stack.dequeue()
print(queue_stack.peek())

#5
class Node2:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new = Node2(val)

        if self.root is None:
            self.root = new
            return

        cur = self.root

        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = new
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = new
                    return
                cur = cur.right

    def lca(self, val1, val2):
        cur = self.root

        while cur is not None:
            if val1 < cur.val and val2 < cur.val:
                cur = cur.left

            elif val1 > cur.val and val2 > cur.val:
                cur = cur.right

            else:
                return cur.val
        return None

print("\nTask 5")
tree = BST()

tree.insert(20)
tree.insert(10)
tree.insert(30)
tree.insert(5)
tree.insert(15)
tree.insert(25)
tree.insert(35)

print(tree.lca(5, 15))

#6
class Tree:
    def __init__(self):
        self.root = None

    def count_leaf(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return self.count_leaf(node.left) + self.count_leaf(node.right)

print("\nTask 6")
tree = Tree()

tree.root = Node2(1)
tree.root.left = Node2(2)
tree.root.right = Node2(3)
tree.root.left.left = Node2(4)
tree.root.left.right = Node2(5)
tree.root.right.right = Node2(6)

print(tree.count_leaf(tree.root))


