def max_subarray_sum(nums):
    max_ending_here = max_so_far = nums[0]

    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Test the function
input_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray_sum(input_array)
print(max_sum)  # This will print: 6
