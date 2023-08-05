def get_permutations(s):
    if len(s) <= 1:
        return [s]

    perms = []

    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i + 1:]
        sub_permutations = get_permutations(remaining_chars)

        for perm in sub_permutations:
            perms.append(char + perm)

    return perms



input_string = "abc"
permutations = get_permutations(input_string)
print(permutations)
