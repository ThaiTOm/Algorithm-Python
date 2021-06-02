def is_mersenne_prime(n):
    if n <= 3:
        return n > 2
    if 2**int(math.log(n+1, 2)) - 1 != n:
        return False
    s = 4
    for i in range(int(math.log(n+1, 2)) - 2):
        s = ((s * s) - 2) % n
    return True if s == 0 else False
