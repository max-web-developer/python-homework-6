# Найдите сумму чисел массива, которые расположены до первого четного числа массива. 
# Если четных чисел в массиве нет, 
# то найти сумму всех чисел за исключением крайних.

def sumofelements (given_list):
    total=0
    for number in given_list:
        if number % 2 == 0:
            total=total+number
        else:
            total=given_list[0] + given_list[-1]
    return total
print(sumofelements([2,4,6,12,32]))   
print(sumofelements([3,4,6,11,32]))   


