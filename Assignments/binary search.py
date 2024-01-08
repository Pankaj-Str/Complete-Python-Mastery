# Binary search algorithm
# Author: codeswithpankaj.com

def binary_search(arr, target):
    # Initialize low and high indices for the search range
    low, high = 0, len(arr) - 1

    # Continue searching while the range is valid
    while low <= high:
        # Calculate the middle index and corresponding value
        mid = (low + high) // 2
        mid_value = arr[mid]

        # Check if the middle value is the target
        if mid_value == target:
            return mid  # Target found, return its index
        elif mid_value < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

# Perform binary search
result = binary_search(sorted_list, target_value)

# Display the result
if result != -1:
    print(f'Target {target_value} found at index {result}')
else:
    print(f'Target {target_value} not found in the list')