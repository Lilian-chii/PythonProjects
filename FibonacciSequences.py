def fibonacci_series_generator(n):
    first_value = 0
    second_value = 1
    series = []
    for i in range (n):
        if (i<=1):
            next_value = i
        else:
            next_value = first_value+second_value
            first_value=second_value
            second_value=next_value
        series.append(next_value)
    return series
    
fibonacci_series=fibonacci_series_generator(10)
print(fibonacci_series)








