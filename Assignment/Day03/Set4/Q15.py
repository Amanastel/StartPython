def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test the function
input_array = [4, 1, 2, 1, 2]
single = single_number(input_array)
print(single)  # This will print: 4
