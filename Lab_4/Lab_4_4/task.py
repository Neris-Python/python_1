import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('s7_data_sample_rev4_50k.xlsx')

print("Первые 5 строк данных:")
print(df.head())

date_issue_col = 'ISSUE_DATE'
date_flight_col = 'FLIGHT_DATE_LOC'
amount_col = 'REVENUE_AMOUNT'
departure_airport_col = 'ORIG_CITY_CODE'
passenger_type_col = 'PAX_TYPE'
status_col = 'FFP_FLAG'
payment_method_col = 'FOP_TYPE_CODE'

if date_issue_col in df.columns:
    df[date_issue_col] = pd.to_datetime(df[date_issue_col])
if date_flight_col in df.columns:
    df[date_flight_col] = pd.to_datetime(df[date_flight_col])

print("### Общие описательные статистики")
if amount_col in df.columns:
    print(df.describe())
    print(f"Общий объем продаж: {df[amount_col].sum()} рублей")
    print(f"Количество записей: {len(df)}")

    plt.figure(figsize=(10, 6))
    plt.hist(df[amount_col], bins=50, color='blue', alpha=0.7)
    plt.title('Распределение сумм продаж')
    plt.xlabel('Сумма (руб)')
    plt.ylabel('Частота')
    plt.savefig('histogram_amounts.png')
    plt.show()
else:
    print(f"Столбец '{amount_col}' не найден. Пропускаем.")

print("\n### Анализ аэропортов")
if departure_airport_col in df.columns:
    top_departure = df[departure_airport_col].value_counts().head(5)
    print("Топ-5 аэропортов вылета:")
    print(top_departure)

    plt.figure(figsize=(10, 6))
    top_departure.plot(kind='bar', color='green')
    plt.title('Топ-5 аэропортов вылета')
    plt.xlabel('Аэропорт')
    plt.ylabel('Количество')
    plt.savefig('bar_airports.png')
    plt.show()
else:
    print(f"Столбец '{departure_airport_col}' не найден. Пропускаем.")

print("\n### Сезонность")
if date_issue_col in df.columns and date_flight_col in df.columns and amount_col in df.columns:
    df['month_issue'] = df[date_issue_col].dt.month
    df['month_flight'] = df[date_flight_col].dt.month
    monthly_sales = df.groupby('month_issue')[amount_col].sum()
    monthly_flights = df.groupby('month_flight').size()

    print("Продажи по месяцам (ISSUE_DATE):")
    print(monthly_sales)
    print("Перелеты по месяцам (FLIGHT_DATE_LOC):")
    print(monthly_flights)

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sales.index, monthly_sales.values, label='Продажи (руб)', marker='o')
    plt.plot(monthly_flights.index, monthly_flights.values, label='Количество перелетов', marker='s')
    plt.title('Сезонность продаж и перелетов')
    plt.xlabel('Месяц')
    plt.ylabel('Значение')
    plt.legend()
    plt.savefig('line_seasonality.png')
    plt.show()
else:
    print(f"Столбцы '{date_issue_col}', '{date_flight_col}' или '{amount_col}' не найдены. Пропускаем.")

print("\n### Анализ пассажиров")
if passenger_type_col in df.columns and amount_col in df.columns:
    passenger_stats = df.groupby(passenger_type_col)[amount_col].agg(['mean', 'count'])
    print("Статистики по типам пассажиров:")
    print(passenger_stats)

    plt.figure(figsize=(8, 8))
    df[passenger_type_col].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Распределение типов пассажиров')
    plt.savefig('pie_passengers.png')
    plt.show()
else:
    print(f"Столбцы '{passenger_type_col}' или '{amount_col}' не найдены. Пропускаем.")

if status_col in df.columns and amount_col in df.columns:
    status_stats = df.groupby(status_col)[amount_col].agg(['mean', 'count'])
    print("Статистики по статусу:")
    print(status_stats)
else:
    print(f"Столбцы '{status_col}' или '{amount_col}' не найдены. Пропускаем.")

print("\n### Анализ способов оплаты")
if payment_method_col in df.columns and amount_col in df.columns:
    payment_stats = df.groupby(payment_method_col)[amount_col].agg(['mean', 'count'])
    print("Статистики по способам оплаты:")
    print(payment_stats)

    plt.figure(figsize=(10, 6))
    df[payment_method_col].value_counts().plot(kind='bar', color='orange')
    plt.title('Распределение способов оплаты')
    plt.xlabel('Способ оплаты')
    plt.ylabel('Количество')
    plt.savefig('bar_payments.png')
    plt.show()
else:
    print(f"Столбцы '{payment_method_col}' или '{amount_col}' не найдены. Пропускаем.")

print("\n### Предсказание")
if date_issue_col in df.columns and date_flight_col in df.columns and amount_col in df.columns:
    df['days_issue'] = (df[date_issue_col] - df[date_issue_col].min()).dt.days
    df['days_flight'] = (df[date_flight_col] - df[date_flight_col].min()).dt.days
    X_sales = df['days_issue'].values
    y_sales = df[amount_col].values

    def linear_regression(X, y):
        if len(X) == 0 or np.sum((X - np.mean(X))**2) == 0:
            return 0, np.mean(y) if len(y) > 0 else 0
        X_mean = np.mean(X)
        y_mean = np.mean(y)
        m = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean)**2)
        b = y_mean - m * X_mean
        return m, b

    m_sales, b_sales = linear_regression(X_sales, y_sales)

    flights_agg = df.groupby('days_flight').size().reset_index(name='flights')
    X_flights = flights_agg['days_flight'].values
    y_flights = flights_agg['flights'].values
    m_flights, b_flights = linear_regression(X_flights, y_flights)

    future_days = max(df['days_issue'].max(), df['days_flight'].max()) + 365
    pred_sales = m_sales * future_days + b_sales
    pred_flights = m_flights * future_days + b_flights

    print(f"Предсказание продаж на следующий год: {pred_sales:.0f} рублей")
    print(f"Предсказание перелетов на следующий год: {pred_flights:.0f}")

    plt.figure(figsize=(10, 6))
    plt.scatter(X_sales, y_sales, color='blue', label='Фактические продажи')
    plt.plot(X_sales, m_sales * X_sales + b_sales, color='red', label='Линия регрессии')
    plt.title('Предсказание продаж')
    plt.xlabel('Дни')
    plt.ylabel('Сумма (руб)')
    plt.legend()
    plt.savefig('line_prediction.png')
    plt.show()
else:
    print(f"Столбцы '{date_issue_col}', '{date_flight_col}' или '{amount_col}' не найдены. Пропускаем.")