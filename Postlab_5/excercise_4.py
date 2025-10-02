def sum_until(limit):
    if limit < 1:
        return 0

    total = 0
    for i in range(1,limit+1):
        total += i

    return total
