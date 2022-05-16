'''
Sugar delivery / ver. Dynamic Programming
3 5 6 8 9 10 11 12 13 14 15 -> 점차 더해가는 것
ex) 8 11 14 17... 20부터는 15를 적용
'''

def sugar_dp(num) :
    for i in range (num + 1) :
        if sugar_list[i] != 0 :
            if sugar_list[i + 3] == 0 : 
                sugar_list[i + 3] = sugar_list[i] + 1
            if sugar_list[i + 5] == 0 : 
                sugar_list[i + 5] = sugar_list[i] + 1
        if i == 4995 : 
            break
    return sugar_list[num]

sugar_list = [0 for i in range (5001)]
sugar_list[3] = 1
sugar_list[5] = 1

input_num = int(input())
sugar_num = sugar_dp(input_num)
if sugar_num == 0 :
    print("-1")
else :
    print(sugar_num)