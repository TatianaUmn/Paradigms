# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). 


import random
import math

def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def mean(data):
    return sum(data) / len(data)

def correlation(x, y):
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = math.sqrt(sum((xi - mean_x) ** 2 for xi in x)) * math.sqrt(sum((yi - mean_y) ** 2 for yi in y))
    return numerator / denominator

# Генерация случайных массивов
size = 5
x = generate_random_array(size)
y = generate_random_array(size)

# Расчет корреляции Пирсона
result = correlation(x, y)
print(x)
print(y)
print("Корреляция Пирсона:", result)