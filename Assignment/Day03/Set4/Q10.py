def contains_duplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

input_array = [1, 2, 3, 1, 4]
result = contains_duplicate(input_array)
print(result)
