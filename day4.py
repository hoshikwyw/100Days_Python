
def compare_numbers(a, b):
    """
    Compare two numbers and return a string indicating the relationship.
    
    Args:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    str: A string indicating whether a is less than, equal to, or greater than b.
    """
    if a < b:
        return f"{a} is less than {b}"
    elif a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{a} is equal to {b}"

# Example usage:
# print(compare_numbers(3, 5))  # Output: "3 is less than 5"
# print(compare_numbers(10, 10))  # Output: "10 is equal to 10"
# print(compare_numbers(7, 2))  # Output: "7 is greater than 2"
