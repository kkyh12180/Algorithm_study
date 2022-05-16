def drink_wine(list, base_list, num) :
    # Base
    # 0 means can jump 1 or 2
    # 1 means can only jump 2

    '''
    Ref_page : https://mygumi.tistory.com/98
    
    # Answer
    1. Think best value when N
    list[n] = list[n - 2] + base[n]
    >> jump!
    list[n] = list[n - 3] + base[n - 1] + base[n]
    >> Not jump.
    >> Compare them.

    2. We can pass twice.
    And compare list[n -1], list[n]
    '''

    if num > 3 :
        list[0] = base_list[0]
        list[1] = base_list[0] + base_list[1]
        list[2] = max(max(base_list[0] + base_list[2], base_list[1] + base_list[2]), list[1])

        for i in range(3, num) :
            list[i] = max(list[i - 2] + base_list[i], list[i - 3] + base_list[i - 1] + base_list[i])
            list[i] = max(list[i], list[i - 1])
    elif num == 1 :
        list[0] = base_list[0]
    elif num == 2 :
        list[1] = base_list[0] + base_list[1]
    elif num == 3 :
        list[0] = base_list[0]
        list[1] = base_list[0] + base_list[1]
        list[2] = max(max(base_list[0] + base_list[2], base_list[1] + base_list[2]), list[1])

    return list[num - 1]


size = int(input())
base_list = []
for x in range(size) :
    num = int(input())
    base_list.append(num)

list = [0 for x in range(size)]
max_wine = drink_wine(list, base_list, size)

print(max_wine)