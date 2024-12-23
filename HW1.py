#Скачайте любой датасет с сайта https://www.kaggle.com/datasets

# Загрузите набор данных из CSV-файла в DataFrame.
#Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
#Выведите информацию о данных (.info()) и статистическое описание (.describe()).
#2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз

import pandas as pd

df = pd.read_csv("Billionaires.csv")
print("1)")
print(df.head())

print(df.info())

print(df.describe())



print("2)")

df = pd.read_csv("dz.csv")



City = df.groupby("City")["Salary"].mean()

print(group)