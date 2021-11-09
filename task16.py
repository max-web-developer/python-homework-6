# Среди элементов с нечетными индексами найдите наибольший элемент массива, который делится на 3.
def SearchMaxeelemthatsharesonThree(given_list):
    maxN=max(given_list)
    for x in given_list:
        if maxN%3==0:
            return maxN
print(SearchMaxeelemthatsharesonThree([1,2,3,4,5,21,36]))