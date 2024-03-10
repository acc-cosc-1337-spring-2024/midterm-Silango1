def get_sum_of_evens(num):
    """Sums the even numbers up to and including num."""
    total = 0
    for i in range(2, num+1, 2):  # Start from 2, go up to num (inclusive), step by 2 for even numbers
        total += i
    return total
