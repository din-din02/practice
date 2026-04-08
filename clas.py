import pandas as pd#Библиотеки
import matplotlib.pyplot as plt
from log import logging

class BigMacStats:#Класс
    @logging #логгер
    def __init__(self, filepath):#конструктор
        self.data = pd.read_csv(filepath)#загрузка данных 
        self.data = self.data[['name', 'dollar_price']].dropna()
    def grafic(self):#метод
        grouped = self.data.groupby('name')['dollar_price'].mean().sort_values()#группируем, вычисляем среднюю цену, расставляем по возрастанию
        
        if len(grouped) > 20:# выбираем только 20 стран
            grouped = grouped.tail(20)# берем самые дорогие
        
        fig, ax = plt.subplots(figsize=(12, 8))#  график
        a = ax.barh(grouped.index, grouped.values, color='steelblue', edgecolor='black', linewidth=0.5, height=0.6)#цвет для столбцов
        for bar, value in zip(a, grouped.values):# Добавляем значения
            ax.text(value + 0.05, bar.get_y() + bar.get_height()/2, f'${value:.2f}', va='center', fontsize=9)
        
        ax.set_title('Средняя стоимость Бигмака по странам', fontsize=14, fontweight='bold', pad=15)# подписи
        ax.set_xlabel('Стоимость (USD)', fontsize=11)
        ax.set_ylabel('Страны', fontsize=11)
        ax.grid(axis='x', alpha=0.3, linestyle='--')#  сетка по оси X
        ax.set_axisbelow(True)
        #Отрисовка
        plt.tight_layout()
        plt.show()
