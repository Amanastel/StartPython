from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q1.put(item)

    def pop(self):
        if self.q1.empty():
            return None

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        top_item = self.q1.get()

        self.q1, self.q2 = self.q2, self.q1

        return top_item

# Test the StackUsingQueue class
stack = StackUsingQueue()
output = []

stack.push(1)
output.append(stack.pop())

stack.push(2)
output.append(stack.pop())

stack.push(3)
output.append(stack.pop())
output.append(stack.pop())
output.append(stack.pop())

print(", ".join(map(str, output)))
