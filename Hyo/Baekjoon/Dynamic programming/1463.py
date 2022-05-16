'''
x % 3 == 0 -> x / 3 or x - 1
x % 2 == 0 -> x / 2 or x - 1
'''

def make_one(num) : 
    for i in range(2, num + 1) :
        # i + 1
        if i != 1000000 and one_list[i + 1] == 0 : 
            one_list[i + 1] = one_list[i] + 1
        elif i != 1000000 and one_list[i + 1] > (one_list[i] + 1) :
            one_list[i + 1] = one_list[i] + 1
        
        # i * 2
        if (i < 500001) and one_list[i * 2] == 0 :
            one_list[i * 2] = one_list[i] + 1
        elif (i < 500001) and  one_list[i * 2] > (one_list[i] + 1) :
            one_list[i * 2] = one_list[i] + 1
        
        # i * 3
        if (i < 333334) and one_list[i * 3] == 0 :
            one_list[i * 3] = one_list[i] + 1
        elif (i < 333334) and  one_list[i * 3] > (one_list[i] + 1) :
            one_list[i * 3] = one_list[i] + 1
    return one_list[num]

one_list = [0 for x in range(1000001)]
one_list[2] = 1
one_list[3] = 1

input_num = int(input())
print(make_one(input_num))