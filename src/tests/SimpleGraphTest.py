import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

def draw(timestamps, values):
    # Преобразование timestamp в объекты datetime
    datetimes = [datetime.utcfromtimestamp(ts) for ts in timestamps]

    # Создание графика
    plt.figure(figsize=(10, 6))
    plt.plot(datetimes, values, marker='o')

    # Настройка формата времени на оси X
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    # Поворот меток времени для лучшей читаемости
    plt.gcf().autofmt_xdate()

    #Наименование осей и графика

    plt.xlabel('Время')
    plt.ylabel('Температура')
    plt.title('Погода')
    plt.grid(True)

    # Отображение графика
    plt.show()
    #сохраняем в файл
#     plt.savefig("graph.png")