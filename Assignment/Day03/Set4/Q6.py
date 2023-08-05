def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = total_sum - actual_sum
    return missing_number


input_array = [3, 0, 1]
missing_num = find_missing_number(input_array)
print(missing_num)
