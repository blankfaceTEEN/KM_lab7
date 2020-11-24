from statistics import mode, median

import matplotlib.pyplot as plt
import numpy as np


def calculate(values):
    print('Значения:', values)
    print('\nМатематическое ожидание:', np.mean(values))
    print('Дисперсия:', np.var(values))
    print('Выборочное среднее:', np.sum(values) / len(values))
    print('Среднее квадратичное отклонение:', np.std(values))
    print('Размах:', max(values) - min(values))
    print('Мода:', mode(values))
    print('Медиана:', median(values))

    plt.hist(values, bins=5, edgecolor='black')
    plt.xlabel('Числа')
    plt.ylabel('Частота')
    plt.show()
