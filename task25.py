# Определите, можно ли вычеркнуть из данного массива одно число так, 
# чтобы оставшиеся числа оказались упорядоченными по возрастанию.

def multi_delete(list_):
     indexes =int(input('what index you wanna to remove?; '))
     for index in indexes: 
         del list_[index] 
     return list_
print(multi_delete([1,2,4,5,6,6,7,7]))