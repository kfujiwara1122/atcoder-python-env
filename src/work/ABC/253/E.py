MOD = 998244353
N, M, K = list(map(int, input().split()))
if K == 0:
    print(M**N % MOD)
    exit()
dp = [[0] * (M + 1) for _ in range(N)]
for i in range(1, M + 1):
    dp[0][i] = 1


def cum(n):
    global dp
    for i in range(1, M + 1):
        dp[n][i] += dp[n][i - 1]
        dp[n][i] %= MOD


cum(0)
for n in range(1, N):
    for m in range(1, M + 1):
        lb = m - K
        ub = m + K
        if lb > 0:
            dp[n][m] += dp[n - 1][lb]
        if ub <= M:
            dp[n][m] += dp[n - 1][M] - dp[n - 1][ub - 1]
        dp[n][m] %= MOD
    cum(n)
print(dp[N - 1][M] % MOD)
