# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений в порядке 
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 25
# 3 6 9 12 15 18


import random
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
set_1 = set()
set_2 = set()
for i in range(a):
    set_1.add(random.randint(1,10))
for i in range(b):
    set_2.add(random.randint(1,10))
set_3 = list(set_1.intersection(set_2))
set_3.sort()
print(*set_3)