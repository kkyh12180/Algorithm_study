'''
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
'''


def w(a, b, c) :
    if a <= 0 or b <= 0 or c <= 0 : 
        return 1
    
    if a > 20 or b > 20 or c > 20 : 
        return w(20, 20, 20)

    if w_list[a][b][c] != 0 :
        return w_list[a][b][c]

    if a < b and b < c :
        w_list[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else :
        w_list[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    
    return w_list[a][b][c] 


w_list = [[[0 for X in range(21)] for Y in range(21)] for Z in range(21)]

while True :
    x, y, z = map(int, input().split())

    if x == -1 and y == -1 and z == -1 :
        break
    print(f'w({x}, {y}, {z}) = {w(x, y, z)}')