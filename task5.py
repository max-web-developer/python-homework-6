# Создать массив из n первых чисел Фибоначчи.
# (Тут у пользователя спрашивается сколько чисел Фибоначчи должно присутствовать в массиве, 
# и далее циклом нужно вычислить каждый член этой последовательности и внести в список)

FibN = int(input('how many numbers ypu want to have? '))
list = [1, 1]
prev = list[0]
next = list[1]
for i in range(2,FibN,1):
    newNext=prev + next
    list.append(newNext)
    prev = next
    next = newNext
print(list)


