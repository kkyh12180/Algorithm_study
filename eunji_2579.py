# 0510 알고 스터디 2회차
# https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%802579%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0-DP

n = int(input())
arr = [0]
for i in range(n):
    arr.append(int(input()))

dp = [0] * (n+1)

if n == 1:
    print(arr[1])
else:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

    print(dp[n])
