#  Нужно посчитать сумму всех елементов масива!
def Sumnums(a):
    total=0
    total2=1
    for number in a:
        total=total+number
        total2=total2*number
    return total,total2
print(Sumnums([1,2,3,4,22,1]))