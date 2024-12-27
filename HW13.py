# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
#
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
#
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
#
# Приклад:
#
# Copy code
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA



import string
inputs=("a-c","a-a","s-H","a-A")
letters = string.ascii_letters

# Обрабатываем каждый интервал отдельно
for user_input in inputs:
    # разделяем первую и последнюю букву
    start, end = user_input.split("-")

    # получаем индексы первой последней буквыи
    start_index = letters.index(start)
    end_index = letters.index(end)

    # вытаскиваем последовательность букв
    result = letters[start_index:end_index + 1]

    # Вывод результата
    print(f"{user_input} -> {result}")