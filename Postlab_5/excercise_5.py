def calculate_series_sum(start_number, num_terms):
    total = 0
    for i in range(num_terms):
        total += (start_number + i)
    return total