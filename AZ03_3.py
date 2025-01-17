import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Парсинг цен на диваны с divan.ru
url = "https://www.divan.ru/perm/category/divany"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Извлечение данных о диванах
divans = []
prices = []

for item in soup.find_all('div', class_='LlPhw'):
    name = item.find('span', itemprop='name').get_text(strip=True)
    price = item.find('span', class_='ui-LD-ZU KIkOH').get_text(strip=True)
    price = int(''.join(filter(str.isdigit, price)))  # Преобразование цены в число
    divans.append(name)
    prices.append(price)

# Сохранение данных в DataFrame
data = pd.DataFrame({'Название дивана': divans, 'Цена': prices})
data.to_csv('divan_prices.csv', index=False)

# Вычисление средней цены
average_price = data['Цена'].mean()
print(f"Средняя цена на диваны: {average_price}")

# Построение гистограммы цен
plt.hist(data['Цена'], bins=20, color='orange', edgecolor='black', alpha=0.7)
plt.title("Гистограмма цен на диваны")
plt.xlabel("Цена")
plt.ylabel("Частота")
plt.grid(True)
plt.show()