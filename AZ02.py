import pandas as pd

# Данные
data = {
    "Имя ученика": ["Анна", "Борис", "Виктория", "Глеб", "Даниил", "Екатерина", "Зоя", "Иван", "Ксения", "Лев"],
    "Математика": [4, 3, 5, 4, 3, 5, 4, 4, 5, 4],
    "Физика": [4, 4, 5, 4, 3, 5, 4, 3, 4, 4],
    "Химия": [3, 4, 4, 3, 3, 5, 5, 3, 4, 4],
    "Литература": [5, 4, 5, 4, 4, 5, 5, 5, 5, 5],
    "История": [4, 3, 5, 4, 4, 5, 4, 4, 5, 4]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Вывод первых нескольких строк DataFrame
print("Первые строки DataFrame:")
print(df.head())

# Вычисление средней оценки по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"\nQ1 для математики: {Q1_math}")
print(f"Q3 для математики: {Q3_math}")

# Расчёт IQR (межквартильный размах)
IQR_math = Q3_math - Q1_math
print(f"IQR для математики: {IQR_math}")

# Вычисление стандартного отклонения по каждому предмету
std_dev_scores = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev_scores)

