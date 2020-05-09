#1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из
# первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random).

print("Задание №1")
import random

list_names = ['Дима', 'Саша', 'Вадим', 'Александр', 'Светлана', 'Антон', 'Денис', 'Лина', 'Алина', 'Юлия', 'Кристина', 'Вадим', 'Ксюша', 'Петя', 'Андрей', 'Максим', 'Владимир', 'Николай', 'Егор', 'Евгений']

def name_n(list_names, n):
    list_names_random = []
    len_list = len(list_names)
    newName = ''

    for i in range(1, n + 1):
        randomChoice = random.randint(0, len_list-1)
        newName = list_names[randomChoice]
        list_names_random.append(newName)

    return list_names_random

list_names_random = name_n(list_names, 100)

print('Список рандомных 100 имен:')
print(list_names_random)
print()

#2. Напишите функцию вывода самого частого имени из списка на выходе функции F.
print('Задание № 2')

from collections import Counter

def max_count(lst):
    count = Counter(lst)
    return max(count, key=lambda x: count[x])

#print(*Counter(list_names_random).most_common(1))
print('Самое популярное имя из списка:')
print(max_count(list_names_random))
print()

#print(max(list_names_random, key=list_names_random.count)) # Вариант, если без функции это делать.

#3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
print('Задание № 3')
def r_letter(lst):
    lst = map(lambda x: x[0], lst) # Создаем список из первых букв
    return Counter(lst).most_common()[-1:][0][0]

print('Самая редкая первая буква и имени:')
print(r_letter(list_names_random))
print()

#4. В файле с логами найти дату самого позднего лога (по метке времени)
print('Задание №4')
with open('log', mode='rt', encoding='utf-8') as f:
    text = f.read()
print(text, '\n')

text = text.split('\n')
last_log = max(text, key=lambda x: x[:23])
print('Last log:', last_log)