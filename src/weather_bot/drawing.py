import matplotlib.pyplot as plt

def draw_graph(timestamps, values) -> None:
    '''Рисует график по полученным значениям осей'''
    # Создание графика
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, values, marker='o')

    # Поворот меток времени для лучшей читаемости
    plt.gcf().autofmt_xdate()

    #Наименование осей и графика
    plt.xlabel('Время')
    plt.ylabel('Температура')
    plt.title('Погода')
    plt.grid(True)

    #сохраняем в файл
    plt.savefig('weather_bot/graphs/graph.png')