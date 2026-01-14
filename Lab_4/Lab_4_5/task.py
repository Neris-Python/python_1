import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('lab_4_part_5.xlsx', header=1)

df.drop('Unnamed: 0', axis=1, inplace=True)

print("\nОбзор данных:")
print(df.head())
print("\nСтатистика:")
print(df.describe())
df.to_csv('data.csv', index=False)

date_col = 'Дата'
year_col = 'Год'
year_month_col = 'Год-мес'
point_col = 'точка'
brand_col = 'бренд'
product_col = 'товар'
quantity_col = 'Количество'
sales_col = 'Продажи'
cost_col = 'Себестоимость'

df['Прибыль'] = df[sales_col] - df[cost_col]
df['Средняя цена'] = df[sales_col] / df[quantity_col]

products = df[product_col].unique()
locations = df[point_col].unique()

total_turnover = df.groupby(date_col)[sales_col].sum()
plt.figure(figsize=(12, 6))
plt.plot(total_turnover.index, total_turnover.values, marker='o')
plt.title('Динамика общего товарооборота')
plt.xlabel('Дата')
plt.ylabel('Продажи (руб.)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

for product in products[:5]:
    product_data = df[df[product_col] == product]

    qty_by_date = product_data.groupby(date_col)[quantity_col].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(qty_by_date.index, qty_by_date.values, marker='o', label='Количество')
    plt.title(f'Динамика количества продаж для {product}')
    plt.xlabel('Дата')
    plt.ylabel('Количество')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    volume_by_date = product_data.groupby(date_col)[sales_col].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(volume_by_date.index, volume_by_date.values, marker='o', color='green')
    plt.title(f'Динамика объема продаж для {product}')
    plt.xlabel('Дата')
    plt.ylabel('Продажи (руб.)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    avg_price_by_date = product_data.groupby(date_col)['Средняя цена'].mean()
    plt.figure(figsize=(10, 5))
    plt.plot(avg_price_by_date.index, avg_price_by_date.values, marker='o', color='red')
    plt.title(f'Динамика средней цены для {product}')
    plt.xlabel('Дата')
    plt.ylabel('Средняя цена (руб.)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

for location in locations:
    location_data = df[df[point_col] == location]

    avg_sales_by_date = location_data.groupby(date_col)[sales_col].mean()
    plt.figure(figsize=(10, 5))
    plt.plot(avg_sales_by_date.index, avg_sales_by_date.values, marker='o', color='blue')
    plt.title(f'Средние продажи на точку {location}')
    plt.xlabel('Дата')
    plt.ylabel('Средние продажи (руб.)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    pct_change = avg_sales_by_date.pct_change() * 100
    plt.figure(figsize=(10, 5))
    plt.plot(pct_change.index, pct_change.values, marker='o', color='purple')
    plt.title(f'Рост/спад продаж на точке {location} (%)')
    plt.xlabel('Дата')
    plt.ylabel('Процентное изменение')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

total_cost = df.groupby(date_col)[cost_col].sum()
total_profit = df.groupby(date_col)['Прибыль'].sum()
plt.figure(figsize=(12, 6))
plt.plot(total_cost.index, total_cost.values, label='Себестоимость', marker='o')
plt.plot(total_profit.index, total_profit.values, label='Прибыль', marker='o')
plt.title('Динамика себестоимости и прибыли')
plt.xlabel('Дата')
plt.ylabel('Руб.')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

forecast_period = 12
for product in products[:5]:
    product_data = df[df[product_col] == product].groupby(date_col)[sales_col].sum().reset_index()
    if len(product_data) > 1:
        product_data['Время'] = np.arange(len(product_data))

        X = product_data['Время'].values
        y = product_data[sales_col].values

        coeffs = np.polyfit(X, y, 1)
        poly = np.poly1d(coeffs)

        future_times = np.arange(len(product_data), len(product_data) + forecast_period)
        predictions = poly(future_times)

        plt.figure(figsize=(10, 5))
        plt.plot(product_data[date_col], y, marker='o', label='Исторические данные')
        future_dates = pd.date_range(start=product_data[date_col].max() + pd.DateOffset(months=1),
                                     periods=forecast_period, freq='M')
        plt.plot(future_dates, predictions, marker='o', linestyle='--', color='red', label='Прогноз')
        plt.title(f'Прогноз объема продаж для {product}')
        plt.xlabel('Дата')
        plt.ylabel('Продажи (руб.)')
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

        y_pred = poly(X)
        mse = np.mean((y - y_pred) ** 2)
        print(f'MSE для {product}: {mse:.2f}')
    else:
        print(f'Недостаточно данных для прогноза {product}')
