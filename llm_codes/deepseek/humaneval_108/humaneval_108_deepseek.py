def count_nums(arr):
    count = 0
    for num in arr:
        s = str(num)
        total = 0
        i = 0
        if s[0] == '-':
            # The first digit after '-' is negative
            if len(s) > 1:
                total += -int(s[1])
            i = 2
        else:
            i = 0
        # Process remaining digits
        while i < len(s):
            total += int(s[i])
            i += 1
        if total > 0:
            count += 1
    return count
