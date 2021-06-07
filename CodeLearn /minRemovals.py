def minRemovals(arr, k):
    n = len(arr)
    arr.sort()
    dp = [0 for i in range(n)]
    for i in range(n):
        dp[i] = -1
    ans = n - 1
    dp[0] = 0
    for i in range(1, n):
        dp[i] = i
        j = dp[i - 1]
        while (j != i and arr[i] - arr[j] > k):
            j += 1
        dp[i] = min(dp[i], j)
        ans = min(ans, (n - (i - j + 1)))
        print(ans)
    return ans


minRemovals([1, 7, 14, 0, 9, 4, 18, 18, 2, 4], 4
            )
