import random
def qwe(num, m):
    list = []
    list.append(num)
    for i in m - 2:
        list.append((list[i]+num)/random.randint(1,11))
    return list[m-1]
#не совсем понятно что должна возвращать функция, по этому последний элемент

print(qwe(2,5))
