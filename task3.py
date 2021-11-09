
# Есть список строк, нужно удалить из него все пустые строки
names=[]
while True:
    name=input('enter your name: ')
    if name.strip() == '':
        break
    else: names.append(name.strip().capitalize())


reversed_names = []
for i in range(len(names)-1,-1,-1):
    reversed_names.append(names[i])

print(reversed_names)   
