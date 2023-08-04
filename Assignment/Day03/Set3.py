
# Q1
people = [("John", 25), ("Jane", 30)]

for name, age in people:
    print(f"{name} is {age} years old.")

# Q2

def add_name_age(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age
    else:
        print(f"{name} not found in the dictionary.")

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]
    else:
        print(f"{name} not found in the dictionary.")

# Initial dictionary
people = {}

# Add name-age pairs
add_name_age(people, "John", 25)

# Print the dictionary
print(people)

# Update age
update_age(people, "John", 26)

# Print the dictionary
print(people)

# Delete name
delete_name(people, "John")

# Print the dictionary
print(people)


# Q3
def two_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return None

# Input array and target
nums = [2, 7, 11, 15]
target = 9

# Find the two integers that sum to the target
result = two_sum(nums, target)

if result is not None:
    print(result)
else:
    print("No solution found.")


# Q4
def is_palindrome(word):
    word = word.lower()  # Convert to lowercase to make the comparison case-insensitive
    cleaned_word = ''.join(char for char in word if char.isalnum())  # Remove non-alphanumeric characters

    reversed_word = cleaned_word[::-1]

    if cleaned_word == reversed_word:
        return True
    else:
        return False


# Test the function
input_word = "madam"
if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")



# Q5
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Test the function
input_array = [64, 25, 12, 22, 11]
selection_sort(input_array)
print(input_array)


# Q6
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


# Q7
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=", ")
    elif num % 3 == 0:
        print("Fizz", end=", ")
    elif num % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(num, end=", ")


# Q8
# Read the input file and count words
with open("input.txt", "r") as file:
    content = file.read()
    words = content.split()
    num_words = len(words)

# Write the word count to the output file
with open("output.txt", "w") as file:
    file.write(f"Number of words: {num_words}")


# Q9
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Test the function
num1 = 5
num2 = 0

division_result = divide_numbers(num1, num2)
print(division_result)
