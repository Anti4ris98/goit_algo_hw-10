import pulp

# Ініціалізуємо модель оптимізації
model = pulp.LpProblem("Optimization", pulp.LpMaximize)

# Оголошуємо змінні рішення - кількість "Лимонаду" та "Фруктового соку"
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Додаємо обмеження ресурсів відповідно до нових вимог
model += 2 * lemonade + 1 * fruit_juice <= 100  # Вода
model += 1 * lemonade <= 50  # Цукор
model += 1 * lemonade <= 30  # Лимонний сік
model += 2 * fruit_juice <= 40  # Фруктове пюре

model += lemonade + fruit_juice
model.solve()

print("Кількість виробленого Лимонаду:", pulp.value(lemonade))
print("Кількість виробленого Фруктового соку:", pulp.value(fruit_juice))
