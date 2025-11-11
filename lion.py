from collections import Counter
import docx
import pandas as pd
import matplotlib.pyplot as plt

doc = docx.Document('lion.docx')  # открываем Word
text = ' '.join([k.text for k in doc.paragraphs])  # преобразуем весь текст в одну строку

bukvi = '.,!?;:"()[]{}«»—'  # знаков препинания, которые удалим
for z in bukvi:
    text = text.replace(z, '')  # удаляем каждый знак препинания из текста

words = text.split()  # разбиваем текст на слова
schetchik_slov = Counter(words)  # считаем сколько раз встречается каждое слово
kolichestvo_slov = len(words)  # общее количество слов в тексте

spisok_slov = [(slovo, kolichestvo, (kolichestvo / kolichestvo_slov) * 100) for slovo, kolichestvo in schetchik_slov.items()]
pd.DataFrame(spisok_slov, columns=['Слово', 'Количество', 'Частота (%)']).to_excel('slova.xlsx', index=False)  # сохраняем в Excel

russkie_bukvi = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # строка с русским алфавитом
bukvi = [i for i in text if i in russkie_bukvi]  # отбираем только русские буквы
schetchik_bukv = Counter(bukvi)  # считаем частоту каждой буквы

plt.bar(schetchik_bukv.keys(), schetchik_bukv.values())  # создаем столбчатую диаграмму
plt.ylabel('Количество')  # подпись для  оси игрик
plt.xlabel('Буквы')  # подпись для горизонтальной оси икс
plt.show()  # показываем график

for bukva, kolichestvo in schetchik_bukv.items():
    print(f"{bukva}: {kolichestvo}")  # печатаем статистику