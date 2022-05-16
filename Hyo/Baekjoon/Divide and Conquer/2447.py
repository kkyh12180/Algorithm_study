'''
  0 1 2 3 4 5 6 7 8    0 1 2
0 * * * * * * * * *  0 * * *
1 * * * * * * * * *  1 *   *
2 * * * * * * * * *  2 * * *
3 * * *       * * *  
4 * * *       * * *  start from 1
5 * * *       * * *
6 * * * * * * * * *
7 * * * * * * * * *
8 * * * * * * * * *

start from 3, end at 5
'''

# Conquer block
def conquer_one_block(size, start_x, start_y, list) :
    for i in range(start_x, start_x + size) :
        for j in range(start_y, start_y + size) :
            list[i][j] = 1

    for i in range(start_x + int(size / 3), start_x + int(size / 3) + int(size / 3)) :
        for j in range(start_y + int(size / 3), start_y + int(size / 3) + int(size / 3)) :
            list[i][j] = 0

    return list

def make_star_list(size, start_x, start_y, list) :
    if size == 3 :
        conquer_one_block(size, start_x, start_y, list)
        return list
    else :
        conquer_one_block(size, start_x, start_y, list)

        # Divide list
        for i in range(0, 3) :
            for j in range(0, 3) :
                if i == 1 and j == 1 : 
                    continue
                else :
                    make_star_list(int(size / 3) , start_x + i * int(size / 3), start_y + j * int(size / 3), list)
                    '''
                    # Check list
                    print_stars(list)
                    '''

    return list

def print_stars(list) :
    for i in list :
        for j in i :
            if j == 1 :
                print("*", end = '')
            else :
                print(" ", end = '')
        print()

size = int(input())
test_list = [[0 for x in range(size)] for y in range(size)]
make_star_list(size, 0, 0, test_list)
print_stars(test_list)