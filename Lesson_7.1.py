
# функция которая принимает operation,
# а также количество строк num_rows и количество столбцов num_columns
def print_operation_table(operation, num_rows=9, num_columns=9): 

    # Проверяем размерность таблицы, если строки и столбцы  больше 2, выведем 
    # сообщение об ошибке.
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    # Создаем таблицу
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            # Вычисляем значения ячейки с использованием переданной операции
            result = operation(row, col)
            # Выводим значения с пробелом
            print(result, end=" ")
        print()
# Умножаем, выводим таблицу умножения 3x3
print_operation_table(lambda x, y: x * y, 4, 4)
