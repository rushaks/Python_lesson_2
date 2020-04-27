# Задание 1
f = open('text.txt', 'r', encoding='UTF8')
text = f.read()
f.close()

# Задание 2 (методами строк очистить текст от знаков препинания)
text_clean = text.replace(',','').replace('.','').replace('!','').replace('?','').replace('«','').replace('«','').replace('»','').replace('—','')

# Задание 3 (сформировать list со словами (split))
list_text = text_clean.split()

# Задание 4 (привести все слова к нижнему регистру (map))
lower_list = list(map(lambda x:x.lower(),list_text))

# Задание 5 (получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте)
set_text = set(list_text)
dict_temp = {}
for element in set_text:
    dict_temp[element]=list_text.count(element)
print(dict_temp)

# Задание 6 (вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set))
list_d = list(dict_temp.items())
list_d.sort(key=lambda i:i[1], reverse=True)
print(list_d[:5])

# Задание 7 (выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию)
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
n_list = list(map(lambda x: morph.parse(x[0])[0].normal_form, lower_list))
print(n_list)