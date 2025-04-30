def generate_integers(a, b):
    start = min(a, b)
    end = max(a, b)
    result = []
    for num in range(start, end + 1):
        all_even = True
        for digit in str(num):
            if int(digit) % 2 != 0:
                all_even = False
                break
        if all_even:
            result.append(num)
    return result
