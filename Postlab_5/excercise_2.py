def is_power_of_two(n):
    if n <= 0:
        return False
    next_power = 1
    while next_power < n:
        next_power *= 2
    return next_power == n