
# Q1

n = 5  # Number of rows

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()  # Move to the next line after each row


# Q2
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break  # Stop the loop if the number is greater than 500
    if num > 150:
        continue  # Skip the number and move to the next iteration if it's greater than 150
    if num % 5 == 0:
        print(num)


# Q3
s1 = "Ault"
s2 = "Kelly"

middle_index = len(s1) // 2
s3 = s1[:middle_index] + s2 + s1[middle_index:]

print(s3)


# Q4
str1 = "PyNaTive"

lowercase_chars = [char for char in str1 if char.islower()]
uppercase_chars = [char for char in str1 if char.isupper()]

sorted_str = "".join(lowercase_chars + uppercase_chars)

print(sorted_str)

# Q5

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

concatenated_list = []

for i in range(min(len(list1), len(list2))):
    concatenated_list.append(list1[i] + list2[i])

# Adding any leftover items
if len(list1) > len(list2):
    concatenated_list.extend(list1[len(list2):])
else:
    concatenated_list.extend(list2[len(list1):])

print(concatenated_list)

# Q6

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

concatenated_list = []

for item1 in list1:
    for item2 in list2:
        concatenated_list.append(item1 + item2)

print(concatenated_list)


# Q7
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for item1, item2 in zip(list1, reversed(list2)):
    print(item1, item2)


# Q8
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

initialized_dict = {employee: defaults for employee in employees}

print(initialized_dict)


# Q9
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"}

keys = ["name", "salary"]

extracted_dict = {key: sample_dict[key] for key in keys}

print(extracted_dict)


# Q10
tuple1 = (11, [22, 33], 44, 55)

# Convert the tuple to a list
list1 = list(tuple1)

# Modify the first item of the nested list
list1[1][0] = 222

# Convert the list back to a tuple
tuple1 = tuple(list1)

print("tuple1:", tuple1)



# Q11
def get_even_list(list1):
    even_list = [num for num in list1 if num % 2 == 0]
    return even_list
