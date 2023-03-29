def isaperfectnumber(n):
    sum = 0
    p = 1
    while (p < n):
        if ((n % p) == 0):
            sum += p
        p += 1
    if sum == n:
        n=True
        return n
    else:
        n=False
        return False