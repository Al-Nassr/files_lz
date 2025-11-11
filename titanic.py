import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_parquet('titanic.parquet')
data.to_csv('titanic.csv', index=False)  # переход в csv

tablichko = data.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0) # группировка данных
tablichko_procent = tablichko.div(tablichko.sum(axis=1), axis=0) * 100 # переводим в проценты
tablichko_procent.plot(kind='bar', stacked=True)  # делаем столбчатаю диаграмму в процентах
 # вывод графика
plt.title('Статистика выживания на Титанике')  
plt.xlabel('Класс билета')
plt.ylabel('Сколько людей')
plt.legend(['Погибло', 'Спаслось'])
plt.show()  # показываем  график