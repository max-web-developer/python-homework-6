# вывести элементы от 100 до 150 только четные числа!
# task 1
# i=100
# x=[]
# def task4():
#     for i in range(100,151,2):
#         x.append(i)
#     print(x)
# task4()

# task 2 
def Task4(start,end,step):
    list=[]
    for i in range (start,end+1,step):
        list.append(i)
    return list
        
print(Task4(100, 150, 2))
print(Task4(120, 220, 5))
