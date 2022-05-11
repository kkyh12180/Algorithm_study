# 반대로 생각해보기

n = int(input())
num = [0] * 1000001

i = 2

while i <= n:
    num[i] = num[i-1] + 1
    if i % 2 == 0:
        num[i] = min(num[i], num[i//2] + 1)
    if i % 3 == 0:
        num[i] = min(num[i], num[i//3] + 1)
    i += 1

print(num[n])
