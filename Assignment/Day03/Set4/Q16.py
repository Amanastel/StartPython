class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    left, right = 0, len(values) - 1
    while left < right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1

    return True

# Test the function
# Creating a linked list: 1 -> 2 -> 2 -> 1
node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

result = is_palindrome(node1)
print(result)  # This will print: True
# Compare this snippet from Set4/Q7.py:
# def is_palindrome(s):
#     left, right = 0, len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1

#     return True

# # Test the function
# input_string = "racecar"
# result = is_palindrome(input_string)
# print(result)  # This will print: True
# Compare this snippet from Set4/Q5.py:
# def reverse_string(s):
