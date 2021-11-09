# def test():
#     pass
# test()
# empty function!

# def calcsum(a=0,b=0):
#     return a + b

# print(calcsum())

# def calcSum(*nums):
#     sum=0
#     for num in nums:
#         sum+=num
#     return sum
# print(calcSum(1,2,3,4,5,))

# arithmetic(1,2,'plus')

a=int(input('enter firt number! '))
b=int(input('enter second number:'))
operation=input('what oper you want to do:')

def arithmetic(a,b,operation):

    if operation=='plus':
        return a+b
    if operation=='minus':
        return a-b
    if operation=='divide':
        return a/b

print(arithmetic(a, b, operation))


    
    
    