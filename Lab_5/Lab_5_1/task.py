import requests
from bs4 import BeautifulSoup
import csv

cache = {}

def get_page(country):
    if country in cache:
        return cache[country]
    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        cache[country] = response.text
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы для {country}: {e}")
        return None

def clean_number(text):
    if not text:
        return None
    text = text.split('\n')[0].split('(')[0].split('[')[0].strip()
    digits = ""
    for ch in text:
        if ch.isdigit() or ch == ',':
            digits += ch
        elif digits:
            break
    if digits:
        return digits.replace(',', '')
    return None

def extract_first_number(text):
    if not text:
        return None
    text = text.split('\n')[0].split('(')[0].split('[')[0].strip()
    number = ""
    for ch in text:
        if ch.isdigit() or ch == ',':
            number += ch
        elif number:
            break
    if number:
        return number.replace(',', '')
    return None

def parse_info(html):
    if not html:
        return None, None, None
    soup = BeautifulSoup(html, 'html.parser')
    infobox = soup.find('table', class_='infobox')
    if not infobox:
        return None, None, None
    capital = None
    for tr in infobox.find_all('tr'):
        th = tr.find('th')
        td = tr.find('td')
        if not th or not td:
            continue
        header = th.get_text(" ", strip=True).lower()
        if "capital" in header:
            for a in td.find_all('a'):
                text = a.get_text(strip=True)
                href = a.get('href', '') or ''
                if not text:
                    continue
                if '°' in text:
                    continue
                if href.startswith('#'):
                    continue
                if href.startswith('/wiki/'):
                    capital = text
                    break
            if not capital:
                raw = td.get_text(" ", strip=True)
                if '°' in raw:
                    raw = raw.split('°')[0]
                capital = raw.split('\n')[0].split('(')[0].split('[')[0].strip()
            break
    area = None
    area_row = infobox.find('th', string=lambda text: text and 'Area' in text)
    if area_row:
        td = area_row.find_next('td')
        if td:
            area = extract_first_number(td.get_text())
    population = None
    pop_row = infobox.find('th', string=lambda text: text and 'Population' in text)
    if pop_row:
        td = pop_row.find_next('td')
        if td:
            population = extract_first_number(td.get_text())
    return capital, area, population

def main():
    input_file = input("Введите имя входного файла: ").strip()
    output_file = input("Введите имя выходного файла: ").strip()
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            countries = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Входной файл '{input_file}' не найден.")
        return
    if not countries:
        print("Входной файл пуст или не содержит стран.")
        return
    data = []
    for country in countries:
        print(f"Обработка: {country}")
        html = get_page(country)
        capital, area, population = parse_info(html)
        data.append([country, capital, area, population])
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['country', 'city', 'area', 'population'])
        writer.writerows(data)
    print(f"Данные сохранены в '{output_file}'.")

main()
