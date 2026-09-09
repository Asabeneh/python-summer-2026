
def make_square(n):
    """
    Calculate and return the square of a given number.

    Parameters:
    n (int or float): The number to be squared.

    Returns:
    int or float: The square of the input number.
    """
    return n ** 2

def add_two_nums (a, b):
    """
    Calculate and return the sum o two given numbers.

    Parameters:
    a and b (int or float): The numbers to be squared.

    Returns:
    int or float: The sum of the input numbers.
    """
    return a + b

# 1, 2, 3 = 6
def sum_all_nums(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

def sum_all_nums(n):
    """
    Calculate the sum of all integers from 1 up to and including n.

    Parameters:
    n (int): The upper limit of the range (inclusive).

    Returns:
    int: The total sum of the integers.
    """
    return sum(range(1, n + 1))

