import numpy as np
import matplotlib.pyplot as plt

# Дані для графіка (x координати груп, y1 та y2 координати стовпців)
groups = ['', '', '', '', '']
x1 = [6000,12000, 18000, 24000, 30000]
x2 = [5000, 10000, 15000, 20000, 25000]

# Розміщення стовпців для кожної групи
bar_width = 0.35
index = np.arange(len(groups))

# Створення подвійного стовпчикового графіка
plt.barh(index, x1, bar_width, label='Дохід')
plt.barh(index + bar_width, x2, bar_width, label='Зарплата')

# Додавання заголовка та підписів осей
plt.xlabel('Грн')
plt.xticks(index + bar_width / 2, groups)
plt.legend()

# Відображення графіка
plt.show()
