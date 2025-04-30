def even_odd_count(num):
    even = 0
    odd = 0
    num_str = str(abs(num))
    for digit in num_str:
        d = int(digit)
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
