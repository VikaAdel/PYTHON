# Задача No35. Общее обсуждение
# Напишите функцию, которая принимает одно число и проверяет, является ли оно 
# простым Напоминание: Простое число - это число, которое имеет 2 делителя: 1
#  и n(само число) Input: 5 Output: yes
# определить строка(слово) палиндром или нет рекурсией


def palindrom(n):
    if len(n) <= 1:
        return True
    if n[0] == n[-1]:
        return palindrom(n[1:-1])
    return False
a = str(input("Введите строку: "))
if palindrom(a) == True:
    print("Палиндром")
else:
    print("Не палиндром")