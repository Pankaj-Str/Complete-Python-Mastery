# interchange first and last elements

def interchange_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Example usage
input_list = [1, 2, 3, 4, 5]
interchanged_list = interchange_first_last(input_list)
print(interchanged_list)  # Output: [5, 2, 3, 4, 1]
