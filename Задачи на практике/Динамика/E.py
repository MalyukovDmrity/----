N = int(input())

dp = [[0] * 3 for _ in range(N + 1)]

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1] + dp[i - 1][2]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
    dp[i][2] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]

result = dp[N][0] + dp[N][1] + dp[N][2]

print(result)