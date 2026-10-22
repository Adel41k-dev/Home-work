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
        return self.out_stack.pop()

    def peek(self):
        self._transfer()
        if not self.out_stack:
            raise IndexError("peek from empty queue")
        return self.out_stack[-1]

    def is_empty(self):
        return not self.in_stack and not self.out_stack

queue_stack = QueueUsingStacks()
queue_stack.enqueue(1)
queue_stack.enqueue(2)
queue_stack.enqueue(3)
queue_stack.enqueue(4)
print(queue_stack.in_stack)

#12
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.enqueue(x)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.is_empty():
            return "Error"
        return self.q1.dequeue()

    def peek(self):
        if self.q1.is_empty():
            return "Error, empty stack"
        return self.q1.front()

    def is_empty(self):
        return self.q1.is_empty()

    def printstack(self):
        stackpr = []
        if self.q1.is_empty():
            print("stack is empty")
            return 0
        timeq1 = self.q1.items.copy()
        while timeq1:
            stackpr.append(timeq1.pop())
        print(stackpr)
        return 0



s = StackUsingQueues()

s.printstack()

s.push(1)
s.push(2)
s.push(3)
s.printstack()

s.pop()
s.printstack()

s.push(4)
s.printstack()

print("peek:", s.peek())
print("pop ", s.pop())
print("pop ", s.pop())
print("pop ", s.pop())
s.printstack()
print("is empty? :", s.is_empty())


#13

class Browser:
    def __init__(self):
        self.back_St = []
        self.forward_St = []
        self.current = None

    def visit(self, page):
        if self.current is None:
            self.current = page
            self.forward_St = []
        else:
            self.back_St.append(page)
        print("Visit : ", page)

    def backward(self):
        if not self.back_St:
            print("You cant")
            return

        self.forward_St.append(self.current)
        self.current = self.back_St.pop()
        print("You back to: ", self.current)

    def forward(self):
        if not self.forward_St:
            print("You cant")
            return
        self.back_St.append(self.current)
        self.current = self.forward_St.pop()
        print("You return to: ", self.current)

    def currentpage(self):
        if not self.current:
            return "You dont enter to any site"
        return "Current page: ", self.current

    def history(self):
        print("Back: " , self.back_St)
        print("Current: ", self.current)
        print("Forward: " , self.forward_St)


b = Browser()

b.visit("Google")
b.visit("YouTube")
b.visit("GitHub")
b.history()

print()
b.backward()
b.backward()
b.history()

print()
b.forward()
b.history()

print("\nCurrent page:", b.currentpage())

print()
b.visit("Wikipedia")
b.history()
b.forward()

class Queued:
    def __init__(self):
        self.item = []

    def enqueue(self, data):
        self.item.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Empty queue")
        return self.item.pop(0)

    def is_empty(self):
        return not self.item


class CPU:
    def __init__(self):
        self.queue = Queued()
        self.total_page = 0

    def add_task(self, id_t, student, page):
        self.queue.enqueue([id_t, student, page])
        print(f"Add task: {id_t} {student} - {page}")

    def printqueue(self):
        if self.queue.is_empty():
            print("Queue is empty")
            return
        print("Queue of task:")
        for id_t ,std,pg in self.queue.item:
            print(f"Task {id_t} {std} - {pg} pages")

    def process_all(self):
        order = 1
        while not self.queue.is_empty():
            id_t, student, page = self.queue.dequeue()
            self.total_page += page
            print(f"In proccess task {order} : {id_t} {student} - {page}")
            order+= 1
        print("Total pages: ", self.total_page)

tasks = CPU()
tasks.add_task(1, "Adelt", 10)
tasks.add_task(2, "Batyrkhan", 5)
tasks.add_task(3, "Abylai", 6)
tasks.add_task(4, "Adel", 7)
tasks.printqueue()
tasks.process_all()


class TextEditor:
    def __init__(self):
        self.un_stack = []
        self.re_stack = []

    def write(self, text):
        self.un_stack.append(text)
        self.re_stack = []

    def undo(self):
        if not self.un_stack:
            print("Cant undo")
            return
        self.re_stack.append(self.un_stack.pop())

    def redo(self):
        if not self.re_stack:
            print("Cant redo")
            return
        self.un_stack.append(self.re_stack.pop())

    def showtext(self):
        print("Text:")
        print("".join(self.un_stack))



e = TextEditor()

e.write("Hello")
e.write(" World")
e.showtext()

e.undo()
e.showtext()

e.redo()
e.showtext()


e.undo()
e.undo()
e.undo()
e.showtext()

e.redo()
e.redo()
e.redo()
e.showtext()

e.undo()
e.write("!")
e.showtext()
e.redo()


