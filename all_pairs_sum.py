def find_pairs(numbers, target_value):
    nums_set = set(numbers)

    pairs = []

    for n in nums_set:

        complement = target_value - n

        if complement in nums_set:
            pairs.append({n, complement})

    return pairs


nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Original list of numbers:")
print(nums)
target_val = 35
print("Target value:", target_val)
print("Find all pairs in the said list whose sum is equal to a target value:")
print(find_pairs(nums, target_val))
