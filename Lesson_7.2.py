stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
phrases = stroka.split()
if len(phrases) <= 1:
    print("Количество фраз должно быть больше одной!")
    # Завершаем выполнение программы, так как ритм определить не получится
    exit()
def count_syllables(phrase):
    # Удаляем дефисы и приводим к нижнему регистру для учета различных форм слов
    cleaned_phrase = phrase.replace('-', '').lower()
    # Считаем количество гласных букв
    syllables_count = sum(1 for letter in cleaned_phrase if letter in 'aeiouаеёиоуыэюя')
    return syllables_count

# Подсчитываем слоги в каждой фразе
    syllables_counts = [count_syllables(phrase) for phrase in phrases]
    if all(count == syllables_counts[0] for count in syllables_counts):
        print("Парам пам-пам")
    else:
        print("Пам парам")
