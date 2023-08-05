class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = ListNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

# Test the Stack implementation
stack = Stack()
stack.push(1)
stack.push(2)
pop_result1 = stack.pop()
stack.push(3)
pop_result2 = stack.pop()
pop_result3 = stack.pop()

print(pop_result1)  # Output: 2
print(pop_result2)  # Output: 3
print(pop_result3)  # Output: 1
