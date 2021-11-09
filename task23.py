# Найдите количество различных элементов данного массива.
def count(list):
    newlist = []
    newlist.append(list[0])
    count = False
    for i in list:
        count = False
        for j in newlist:
            if j == i:
                count == True
        if not count:
            newlist.append(i)
    return newlist
print(count([1,2,3,4,5,6,7]))
