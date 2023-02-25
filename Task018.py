# Требуется найти в массиве из случайных чисел(от 1 до n) 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. 
# Последняя строка содержит число X

# *Пример:*
# 5
# -> 1 2 3 4 5
# 6
# -> 5

from random import randint

n = int(input('Введите число элементов: '))

list_1 = list()

for i in range(n):
    list_1.append(randint(1, n))
print('->', *list_1)
list_1 = list(set(list_1))

x = int(input('Введите число для проверки: '))
result = [x]
if list_1.count(x) == 0:
    min = x
    result.clear()
    for i in range(len(list_1)):
        if min >= abs(x - list_1[i]):
            if min > abs(x - list_1[i]):
                result.clear()
            min = abs(x - list_1[i])
            result.append(list_1[i])
print('->', *result)
