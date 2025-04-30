def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        digits = []
        str_num = str(abs(num))
        if num < 0:
            digits.append(-int(str_num[0]))
            digits.extend(int(d) for d in str_num[1:])
        else:
            digits.extend(int(d) for d in str_num)
        
        if sum(digits) > 0:
            count += 1
    return count
