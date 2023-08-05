def climb_stairs(n):
    if n <= 2:
        return n

    prev_step = 1
    curr_step = 2

    for i in range(3, n + 1):
        next_step = prev_step + curr_step
        prev_step, curr_step = curr_step, next_step

    return curr_step



input_steps = 3
distinct_ways = climb_stairs(input_steps)
print(distinct_ways)


# using dynamic programming
def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Test the function
input_steps = 3
distinct_ways = climb_stairs(input_steps)
print(distinct_ways)  # This will print: 3
