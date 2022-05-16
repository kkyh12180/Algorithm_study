'''
Z-explore
1. Divide and Conquer
2. X Changes First

First Try : time out
>> Find "When we should call recursive part"

Solution
>> Find quadrant, and change start_value(cnt)


Second Try : time out
>> Minimize list

Solution
>> Find quadrant, and minimize list
'''

cnt = 0

def z_explore(size, start_x, start_y, target_x, target_y) : 
    global cnt

    if size == 2 :
        # Move Z-Shape
        # list[start_y][start_x] = cnt        
        # print_list(list)
        if start_y == target_y and start_x == target_x :
            return cnt
        cnt = cnt + 1

        # list[start_y][start_x + 1] = cnt
        # print_list(list)
        if start_y == target_y and start_x + 1 == target_x :
            return cnt
        cnt = cnt + 1

        # list[start_y + 1][start_x] = cnt
        # print_list(list)
        if start_y + 1 == target_y and start_x == target_x :
            return cnt
        cnt = cnt + 1
        
        # list[start_y + 1][start_x + 1] = cnt
        # print_list(list)
        if start_y + 1 == target_y and start_x + 1 == target_x :
            return cnt
        cnt = cnt + 1
        
        # If Not Target
        # Problem code
        # return 0
    # Change from here
    else : 
        '''
        # First Code
        # Divide list
        for i in range (0, 2) :
            for j in range (0, 2) :
                # i is Y axis, j is X axis
                # X changes first, then Y changes
                rv = z_explore(int(size / 2), start_x + j * int(size / 2), start_y + i * int(size / 2), list, target_x, target_y)
                # If there is return value, return that
                if rv :
                    return rv
        '''
        
        # Second Code
        # Find quadrant
        point_x = start_x + int(size / 2)
        point_y = start_y + int(size / 2)
        quadrant = 0

        if target_x < point_x and target_y < point_y :
            quadrant = 1
            j = 0
            i = 0
        elif target_x >= point_x and target_y < point_y :
            quadrant = 2
            j = 1
            i = 0
        elif target_x < point_x and target_y >= point_y :
            j = 0
            i = 1
            quadrant = 3
        else : 
            j = 1
            i = 1
            quadrant = 4
        
        cnt = cnt + (quadrant - 1) * (int(size / 2) ** 2)
        rv = z_explore(int(size / 2), start_x + j * int(size / 2), start_y + i * int(size / 2), target_x, target_y)

        if rv :
            return rv
    
def print_list(list) : 
    for i in list :
        for j in i :
            print(j, end=' ')
        print()
    print()

size_expo, target_y, target_x = map(int, input().split())
size = 2 ** size_expo

'''
# First Code
z_list = [[0 for x in range(size)] for y in range(size)]
'''

rv = z_explore(size, 0, 0, target_x, target_y)
print(rv)