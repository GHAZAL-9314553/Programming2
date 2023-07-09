def apply_functions(data, *functions):
    """
    Applies a list of functions to each element in the data list and returns a nested list of results.

    Args:
        data (list): The input data list.
        *functions (callable): Variable number of functions to be applied to each element in the data list.

    Returns:
        list: A nested list containing the results of applying the functions to each element in the data list.
    """
    return [[func(value) for value in data] for func in functions]

data = [1, 2, 3, 4, 5]

# Define the functions to be applied
multiply_by_two = lambda x: x * 2
square = lambda x: x ** 2
add_five = lambda x: x + 5

# Apply the functions to the data
result = apply_functions(data, multiply_by_two, square, add_five)

print(result)
# Output: [[2, 4, 6, 8, 10], [1, 4, 9, 16, 25], [6, 7, 8, 9, 10]]
