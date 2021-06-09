def absolutePermutation(n, k):
    arr = []
    if k*2 > n:
        return -1
    for i in range(1, n+1):
        if i <= k:
            arr.append(i+k)
        elif i > k:
            arr.append(abs(i-k))

    return


absolutePermutation(3, 2)
