def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Test the QuickSort implementation
input_array = [10, 7, 8, 9, 1, 5]
sorted_array = quick_sort(input_array)
print(sorted_array)  # This will print: [1, 5, 7, 8, 9, 10]
