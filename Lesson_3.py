# # В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
#  ценность
# # В случае с английским алфавитом очки распределяются так:

# k = 'ноутбук'

# # # Введите ваше решение ниже

# k = k.upper()
# # print(k)
# # через срез 
# Scrabble = {'AEIOULNSTR':1,
# 'DG':2,
# 'BCMP':3,
# 'FHVWY':4,
# 'K':5,
# 'JX':8,
# 'QZ':10,
# 'АВЕИНОРСТ':1,
# 'ДКЛМПУ':2,
# 'БГЁЬЯ':3,
# 'ЙЫ':4,
# 'ЖЗХЦЧ':5,
# 'ШЭЮ':8,
# 'ФЩЪ':10,}

# sum = 0

# for i in k:
#     #print(i)
#     for key, value in Scrabble.items():
#         #print(key, value)
#         if i in key:
#             sum = sum + value
# print(sum)




# list_1 = [1, 4,  2, 5]
# k = 3


# # Инициализируем переменные для ближайшего элемента и минимальной разницы
# closest_element = list_1[0]
# min_difference = abs(k - list_1[0])


# for element in list_1:
#     # Вычисляем разницу между заданным числом и текущим элементом
#     difference = abs(k - element)

#     # Проверяем, является ли текущий элемент ближе к заданному числу
#     if difference <= min_difference:
#         min_difference = difference
#         closest_element = element

# # Выводим результат, если значение k совпадает с ближайшим элементом
# if min_difference == 0:
#     print(k)
# else:
#     print(closest_element)


# # Пользователь вводит текст(строка). Словом считается
# # последовательность непробельных символов идущих
# # подряд, слова разделены одним или большим числом
# # пробелов. Определите, сколько различных слов
# # содержится в этом тексте.
# # Input: She sells sea shells on the sea shore The shells
# # that she sells are sea shells I'm sure.So if she sells sea
# # shells on the sea shore I'm sure that the shells are sea
# # shore shells
# # Output: 13

# text = input("Введите текст: ")
# # Используем функцию split для разделения текста на слова
# world = text.split()

# # Инициализация множества для хранения уникальных слов
# unique_words_set = set()


# for word in world:
#     cleaned_word = word.strip(".,!?\"'")
#     unique_words_set.add(cleaned_word)

# # Определение количества различных слов
# unique_words_count = len(unique_words_set)

# print(f"Количество различных слов: {unique_words_count}")


# # Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые
#  встречаются в обоих наборах.
# # На вход подается 2 числа через пробел: n m
# # n - кол-во элементов первого множества.
# # m - кол-во элементов второго множества.
# # Затем подаются элементы каждого множества через пробел в виде строки
# var1 = '5 4'
# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'

# # Преобразовываем строки в список чисел, разбиваем строки на подстроки
# set1 = set(map(int, var2.split()))
# set2 = set(map(int, var3.split()))

# # Нахождение пересечения множеств
# common_elements = set1.intersection(set2)

# # Преобразовываем множества в список и сортируем список
# result_list = sorted(list(common_elements))

# result_str = ' '.join(map(str, result_list))
# print(result_str)


# Черника?

arr = [5, 8, 6, 4, 9, 2, 7, 3]
def max_berry_count(arr):
    max_count = 0
    n = len(arr)

    # Шаг 3: Перебор каждого куста
    for i in range(n):
        # Шаг 4: Выбор соседних кустов
        neighbor1 = arr[i] + arr[i - 1] + arr[i - 2]
        neighbor2 = arr[(i + 1) % n]

        # Шаг 5: Максимальное количество ягод для текущего куста
        current_max = max(neighbor1, neighbor2)

        # Шаг 6: Обновление максимального количества ягод
        max_count = max(max_count, current_max)

    # Шаг 7: Вывод результата
    return max_count

# Шаг 8: Вызов функции и вывод результат
result = max_berry_count(arr)
print(f"Максимальное количество ягод, которое может собрать собирающий модуль:{result}")