n = int(input())
# 5kg * x, 3kg * y
# remainder = t1(by 5), t2
x = y = -1
for f in range(n//5+1, 0, -1):
    i = f-1
   # print("i=",i)
    n1 = n-(i*5)
    if n1 == 0:
        x = i
        y = 0
        break
    elif n1 % 3 == 0:
        y = n1//3
        x = i
        break
#print("x=",x,", y=",y)
if x == -1:
    print(-1)
else:
    print(x+y)
