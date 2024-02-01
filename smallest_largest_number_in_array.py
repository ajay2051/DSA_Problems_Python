def find_smallest_largest(arr):
    if not arr:
        return None

    smallest = largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return smallest, largest


smallest_num, largest_num = (find_smallest_largest([2, 7, 5, 4, 3]))
print(f"Smallest Number {smallest_num} ")
print(f"Largest Number {largest_num} ")
