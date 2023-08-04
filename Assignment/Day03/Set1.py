print("Hello, World!")


#  Q2
# Integer
integer_var = 10

# Float
float_var = 3.14

# String
string_var = "Hello, Data Types!"

# Boolean
boolean_var = True

# List
list_var = [1, 2, 3, 4, 5]

# Tuple
tuple_var = (6, 7, 8, 9, 10)

# Dictionary
dict_var = {"key1": "value1", "key2": "value2"}

# Set
set_var = {11, 12, 13, 14, 15}

# Printing types and values
print("Type of integer_var:", type(integer_var), ", value:", integer_var)
print("Type of float_var:", type(float_var), ", value:", float_var)
print("Type of string_var:", type(string_var), ", value:", string_var)
print("Type of boolean_var:", type(boolean_var), ", value:", boolean_var)
print("Type of list_var:", type(list_var), ", value:", list_var)
print("Type of tuple_var:", type(tuple_var), ", value:", tuple_var)
print("Type of dict_var:", type(dict_var), ", value:", dict_var)
print("Type of set_var:", type(set_var), ", value:", set_var)


# Q3

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Add a number
numbers_list.append(20)

# Remove a number
if 5 in numbers_list:
    numbers_list.remove(5)

# Sort the list
numbers_list.sort()

# Print the updated list
print(numbers_list)


# Q4
# Input list of numbers
numbers = [10, 20, 30, 40]

# Calculate sum
sum_numbers = sum(numbers)

# Calculate average
average = sum_numbers / len(numbers)

# Print sum and average
print("Sum:", sum_numbers, ", Average:", average)


# Q5
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Test the function
input_string = "Python"
output_string = reverse_string(input_string)
print(output_string)


# Q6
def count_vowels(input_string):
    vowels = "AEIOUaeiou"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count


# Test the function
input_string = "Hello"
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)


# Q7
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

# Test the function
input_number = 13
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")



# Q8

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
input_number = 5
result = factorial(input_number)
print(f"Factorial of {input_number} is {result}.")


# Q9

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Test the function
input_n = 5
fib_sequence = fibonacci_sequence(input_n)
print(fib_sequence)


squares = [x**2 for x in range(1, 11)]
print(squares)