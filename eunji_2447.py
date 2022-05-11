# 5/10 2회차
paint = [[" "]*6560 for a in range(6560)]


def print_star(n, x, y):
    x = int(x)
    y = int(y)
    n = int(n)
    if n == 1:
        paint[x][y] = "*"
        return
    print_star(n/3, x, y)
    print_star(n/3, x+n/3, y)
    print_star(n/3, x+2*n/3, y)
    print_star(n/3, x, y+n/3)
    print_star(n/3, x+2*n/3, y+n/3)
    print_star(n/3, x, y+2*n/3)
    print_star(n/3, x+n/3, y+2*n/3)
    print_star(n/3, x+2*n/3, y+2*n/3)


N = int(input())
print_star(N, 0, 0)
for i in range(N):
    for j in range(N):
        print(paint[i][j], end='')
    print()
