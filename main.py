# Задача №9.По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! =
#  1 Решить задачу используя цикл while
# Input: 5
# Output: 120

# n = int(input())
# factorial = 1
# while n > 1:
#     #print(factorial)
#     factorial *= n
#     n -= 1
# print(factorial)


# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи 
# оно является, то есть выведите такое число n, что φ(n)=A. Если А не является
#  числом Фибоначчи,
# выведите число -1.
# Input: 5
# Output: 6

# n = input('Номер элемента ряда фибоначи')
# n = int(n)
# f1 = 1
# f2 = 1
# i = 3
# while f1 + f2 <= n:
#     f_sum = f1 + f2
#     f1 = f2
#     f2 = f_sum
#     i = i + 1
# print(f_sum)
# if f_sum == n:
#     print(i)
# else:
#     print(-1)

# Задача №15.  Иван Васильевич пришел на рынок и решил купить два арбуза: один 
# для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
#  Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый 
# тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка
#  содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса 
# соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


# num = int(input('количество арбузов: '))
# num1 = int(input('введите массу арбуза: '))

# min = num1
# max = num1
# while num > 1:
#     num2 = int(input('введите массу арбуза: '))
#     if max < num2:
#         max = num2
#     elif min1 > num2:
#         min1 = num2
    

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числаN.

# N = 16
# stop = 0
# P = 2
# for i in range(N):
#     if stop != 1:
#         P = P ** i
#         if P <= N:
#             print(P, end='\n ')
#             P = 2
#         else:
#             stop = 1
#     else:
#         i = N


# Задача №17. Решение в группах Дан список чисел. Определите, сколько в нем
# встречается различных чисел. Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан
#  изначально.

# lst_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(lst_1)))

# s = 12
# p = 27
# import math
# d = s**2-4*p
# if d >= 0: 
#     x = int((s - math.sqrt(d)) / 2)
#     y = int((s+ math.sqrt(d)) / 2)
# print(f"{x} {y}")



