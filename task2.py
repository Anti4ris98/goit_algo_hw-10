import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))


def monte_carlo_integration(f, a, b, y_max, num_samples=10000):
    count_under_curve = 0
    for _ in range(num_samples):
        x = np.random.uniform(a, b)
        y = np.random.uniform(0, y_max)
        if y < f(x):
            count_under_curve += 1
    area = (b - a) * y_max * (count_under_curve / num_samples)
    return area

# Аналітичне обчислення інтеграла
def analytical_integration(a, b):
    return (1/3) * b**3 - (1/3) * a**3

# Обчислення інтеграла за допомогою scipy
def scipy_integration(f, a, b):
    result, _ = quad(f, a, b)
    return result

# Визначення параметрів
a = 0
b = 2
y_max = f(b)

# Виконання обчислень
monte_carlo_result = monte_carlo_integration(f, a, b, y_max)
analytical_result = analytical_integration(a, b)
scipy_result = scipy_integration(f, a, b)

print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Аналітичний метод: {analytical_result}")
print(f"Функція quad: {scipy_result}")