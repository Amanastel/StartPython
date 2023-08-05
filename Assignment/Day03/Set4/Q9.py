def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Test the function
input_num = 16
result = is_power_of_two(input_num)
print(result)  # This will print: True
