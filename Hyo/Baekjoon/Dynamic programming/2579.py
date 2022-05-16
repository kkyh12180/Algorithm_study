'''
Check Conditions
>> (+ 1) * 2 -> (+ 2)
>> (+ 1) * 1 -> (+ 2) or (+ 1)
>> (+ 2) * 1 -> (+ 1 or + 2)

DP
>> Make Recurrence Relation
>> This will help to make memoization list

Memoiozation?
>> Make Stair List
>> Each Value has maximum of that point
'''

def stair(list, base_list, num) :
    '''
    >> We must include base_list[0] (Top of stair)
    '''
    if num > 3 :
        list[0] = base_list[0]
        list[1] = base_list[0] + base_list[1]
        # Changed from wine, we must include base_list[0]
        list[2] = base_list[0] + base_list[2]

        for i in range(3, num) :
            list[i] = max(list[i - 2] + base_list[i], list[i - 3] + base_list[i - 1] + base_list[i])
    elif num == 1 :
        list[0] = base_list[0]
    elif num == 2 :
        list[1] = base_list[0] + base_list[1]
    elif num == 3 :
        list[0] = base_list[0]
        list[1] = base_list[0] + base_list[1]
        # Changed from wine, we must include base_list[0]
        list[2] = base_list[0] + base_list[2]

    # list[num -1] is not always best.
    # return list[num - 1]
    return max(list)

stairs = int(input())
base_list = []
score_list = [0 for x in range(stairs)]

for i in range(stairs) :
    num = int(input())
    base_list.append(num)

base_list.reverse()
maximum = stair(score_list, base_list, stairs)
print(maximum)