import numpy as np
import matplotlib.pyplot as plt


# Задача 2: Диаграмма рассеяния для двух наборов данных
x_data = np.random.rand(100)  # Набор X
y_data = np.random.rand(100)  # Набор Y

# Построение диаграммы рассеяния
plt.scatter(x_data, y_data, color='green', alpha=0.6)
plt.title("Диаграмма рассеяния")
plt.xlabel("X данные")
plt.ylabel("Y данные")
plt.grid(True)
plt.show()