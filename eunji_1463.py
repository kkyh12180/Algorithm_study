# 5/10 2회차
# 큰 수일 경우 못버팀..
n = int(input())
num = [0] * (n+1)


def cal(index):
    # print("num["+str(index)+"] = "+str(num[index]))
    if index > n:
        return

    if index*2 <= n:
        if num[index*2] == num[index]+1:
            return
        if num[index*2] == 0 or (num[index*2] > num[index]+1):
            num[index*2] = num[index]+1
        cal(index*2)
    if index*3 <= n:
        if num[index*3] == num[index]+1:
            return
        if num[index*3] == 0 or (num[index*3] > num[index]+1):
            num[index*3] = num[index]+1
        cal(index*3)
    if index+1 <= n:
        if num[index+1] == num[index]+1:
            return
        elif num[index+1] == 0 or (num[index+1] > num[index]+1):
            num[index+1] = num[index]+1
        cal(index+1)


cal(1)
print(num[n])
# for t in num[1:n+1]:
#    print(str(t)+" ", end='')
