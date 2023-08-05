def longest_common_prefix(strs):
    if not strs:
        return ""

    strs.sort()

    first_str = strs[0]
    last_str = strs[-1]

    prefix = []
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            prefix.append(first_str[i])
        else:
            break

    return ''.join(prefix)


input_strings = ["flower", "flow", "flight"]
result = longest_common_prefix(input_strings)
print(result)

input_strings = ["apple", "apricot", "appetizer"]
result = longest_common_prefix(input_strings)
print(result)  # This should print: "app"


input_strings = ["cat", "car", "cab"]
result = longest_common_prefix(input_strings)
print(result)  # This should print: "ca"


input_strings = ["dog", "cat", "elephant"]
result = longest_common_prefix(input_strings)
print(result)  # This should print: ""
