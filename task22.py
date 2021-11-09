# Проверьте, является ли данный массив возрастающим или убывающим.
arr=[1,2,3,4,5,56,]
def ordered(arr):
    for i in range(1,len(arr)):
        if arr[i]<=arr[i-1]:
            return False
    return True
print(ordered(arr))

