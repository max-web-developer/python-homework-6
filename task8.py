# Найти количество четных чисел в массиве.
# task 1
# a=[3,4,5,87,44,33,21,22]
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)

# task 2
def odd_even(given_list):
    odd=0
    even=0
    for x in given_list:
        if x%2==0:
            even+=1
        else:
            odd+=1
    return odd , even
print(odd_even([1,3,4,5,6,7]))
