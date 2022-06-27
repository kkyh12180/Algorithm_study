'''
    First try : recursion error
    >> Change to iteration
        >> 01 tiles problem = Make number just using 1 and 2
            = fibonacci

zeros = [0, 0]
one = [1]
case = []
tile_list = []

def zero_one_tile(n) :
    if n < 2 :
        case.append(one)
        tile_list.append(case)
        case.pop()
        return
    if n == 2 :
        # 00 or 11

        # 00 case
        case.append(zeros)
        tile_list.append(case)
        case.pop()

        # 11 case
        case.append(one)
        zero_one_tile(n - 1)
        case.pop()
        return
    # n >= 3
    # 1. test 00
    case.append(zeros)
    zero_one_tile(n - 2)
    case.pop()

    # 2. test 1
    case.append(one)
    zero_one_tile(n - 1)
    case.pop()

    return
'''
num = int(input())

num_list = [1, 2]
for i in range(2, (num + 1)) :
    num_list.append((num_list[i - 1] + num_list[i - 2]) % 15746)

print(num_list[num - 1])