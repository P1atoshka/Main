import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import config

def fetch_price(url):
    response = requests.get(url, headers=config.HEADERS)
    response.raise_for_status()  # Проверка на ошибки HTTP
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Замените селектор на правильный для вашего сайта
    price_element = soup.select_one('.price')  # Пример селектора
    if price_element:
        price_text = price_element.get_text(strip=True)
        return float(price_text.replace('₽', '').replace(' ', '').replace(',', '.'))  # Преобразование в число
    else:
        raise ValueError("Не удалось найти элемент с ценой.")

def save_price_history(price):
    with open('price_history.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d'), price])

def check_price(price):
    if price < config.TARGET_PRICE:
        print(f"ВНИМАНИЕ: Цена товара снизилась до {price}₽!")

def main():
    try:
        current_price = fetch_price(config.URL)
        print(f"Текущая цена: {current_price}₽")
        save_price_history(current_price)
        check_price(current_price)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()