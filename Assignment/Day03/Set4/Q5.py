class QueueUsingStack:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        if self.stack_dequeue:
            return self.stack_dequeue.pop()
        else:
            return None

# Test the implementation
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
dequeue1 = queue.dequeue()
queue.enqueue(3)
dequeue2 = queue.dequeue()
dequeue3 = queue.dequeue()

output = f"{dequeue1}, {dequeue2}, {dequeue3}"
print(output)
