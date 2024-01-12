# Find missing number
def find_missing_number(lst):
    n = len(lst)
    expected_sum = (n + 1) * (n + 2) // 2  # Sum of first (n + 1) natural numbers
    actual_sum = sum(lst)
    missing_number = expected_sum - actual_sum
    return missing_number


# Example usage:
input_list = [1, 2, 3, 5, 6, 7, 8]
result = find_missing_number(input_list)
