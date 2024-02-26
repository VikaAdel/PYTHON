# # Напишите рекурсивную функцию sum(a, b)
a = 3
b = 5
def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a - 1, b + 1)         
    print(sum(a, b))

# # Напишите функцию f, которая на вход принимает два числа a и b, 
# и возводит число a в целую степень b с помощью рекурсии.

# a = 3
# b = 5
# def f(a,b):
#     if b <= 0:
#         return 1
#     else:
#         return a*f(a,b -1)
# print(f(a, b))


# # Холодильники

# def find_infected_fridges():
#     # Вводим количество холодильников
#     n = int(input("Введите количество холодильников: "))
    
#     # Создаем Список для хранения номеров зараженных холодильников
#     infected_fridges = []

#     # Обрабатываем каждый холодильник
#     for fridge_number in range(1, n + 1):
#         # Вводим строку данных для текущего холодильника
#         fridge_data = input(f"Введите данные для холодильника {fridge_number}: ").lower()

#         # Проверяем наличие слова "anton" в строке
#         if "anton" in fridge_data:
#             # Если слово "anton" найдено, добавляем номер холодильника в список
#             infected_fridges.append(str(fridge_number))

#     # Выводим номера зараженных холодильников через пробел
#     if infected_fridges:
#         print("Заражены холодильники с номерами:", " ".join(infected_fridges))
#     else:
#         print("Зараженных холодильников не обнаружено.")

# # Запускаем функцию для поиска зараженных холодильников
# find_infected_fridges()

