sample_list = [['a'], ['b', ['c', 'd', ['e', [10]]]]]


def find_integers(nested_list):
    """Recursively finds and prints all integers within a nested list."""
    integers = []
    for item in nested_list:
        if isinstance(item, int):  # Check if the item is an integer
            integers.append(item)
        elif isinstance(item, list):  # If it's a list, recursively search it
            integers.extend(find_integers(item))
    return integers


# Call the function to find integers in the sample_list
result = find_integers(sample_list)
print(result)
