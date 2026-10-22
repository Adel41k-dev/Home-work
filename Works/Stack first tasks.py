# 1
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
stack = Stack()
for i in range(1, 11):
    stack.push(i)
print(stack.items)
print(stack.pop())
print(stack.peek())
print(stack.isEmpty())
print(stack.size())

# 2
def reverse_string(text):
    stack = []
    for letter in text:
        stack.append(letter)
    result = ""
    while stack:
        result += stack.pop()
    return result
print(reverse_string("HELLO"))

# 3
def is_balanced(expression):
    stack = []
    for symbol in expression:
        if symbol in "([{":
            stack.append(symbol)
        elif symbol in ")]}":
            if not stack:
                return False
            opening = stack.pop()
            if symbol == ")" and opening != "(":
                return False
            if symbol == "]" and opening != "[":
                return False
            if symbol == "}" and opening != "{":
                return False
    return len(stack) == 0
if is_balanced("{[()]}"):
    print("Balanced")
else:
    print("Not balanced")

# 4
def remove_duplicates(text):
    stack = []
    for letter in text:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    return "".join(stack)
print(remove_duplicates("abbaca"))

# 5
def decimal_to_binary(number):
    stack = []
    while number > 0:
        stack.append(number % 2)
        number //= 2
    binary = ""
    while stack:
        binary += str(stack.pop())
    return binary
print(decimal_to_binary(25))

# 6
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def front(self):
        return self.items[0]
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
queue = Queue()
for i in range(1, 11):
    queue.enqueue(i)
print(queue.items)
print(queue.dequeue())
print(queue.dequeue())
print(queue.front())
print(queue.isEmpty())
print(queue.size())
print(queue.items)

# 7
def reverse_queue(queue):
    stack = []
    while queue:
        stack.append(queue.pop(0))
    while stack:
        queue.append(stack.pop())
    return queue
print(reverse_queue([10, 20, 30, 40, 50]))

# 8
def generate_binary_numbers(n):
    queue = ["1"]
    result = []
    for i in range(n):
        number = queue.pop(0)
        result.append(number)
        queue.append(number + "0")
        queue.append(number + "1")
    return result
print(generate_binary_numbers(5))

# 9
def evaluate_postfix(expression):
    stack = []
    for part in expression.split():
        if part in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if part == "+":
                stack.append(a + b)
            elif part == "-":
                stack.append(a - b)
            elif part == "*":
                stack.append(a * b)
            elif part == "/":
                stack.append(a / b)
        else:
            stack.append(int(part))
    return stack.pop()
print(evaluate_postfix("5 3 + 2 *"))

# 10
def infix_to_postfix(expression):
    stack = []
    postfix = []
    priority = {"+": 1, "-": 1, "*": 2, "/": 2}
    for part in expression.split():
        if part.isalnum():
            postfix.append(part)
        elif part == "(":
            stack.append(part)
        elif part == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != "(" and priority[stack[-1]] >= priority[part]:
                postfix.append(stack.pop())
            stack.append(part)
    while stack:
        postfix.append(stack.pop())
    return " ".join(postfix)
print(infix_to_postfix("A + B * C"))