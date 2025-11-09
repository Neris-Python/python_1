import random
import faker
import matplotlib.pyplot as plt
import pandas as pd

fake = faker.Faker('ru_RU')

years = [2021, 2022, 2023, 2024, 2025]
subjects = ['Математика', 'Физика', 'Русский язык', 'История']
specialties = ['Информатика', 'Экономика', 'Юриспруденция', 'Медицина', 'Инженерия']
forms = ['Очная', 'Заочная']

data = []
for year in years:
    for _ in range(5):
        ct_scores = {subj: random.randint(50, 100) for subj in subjects}
        attestat_avg = round(random.uniform(3.0, 10.0), 2)
        total_score = sum(ct_scores.values()) + attestat_avg * 10
        specialty = random.choice(specialties)
        form = random.choice(forms)
        fio = fake.name()
        address = fake.address().replace('\n', ', ')
        phone = fake.phone_number()

        entry = {
            'ФИО': fio,
            'Год поступления': year,
            'Форма обучения': form,
            'Баллы ЦТ/ЦЭ': ct_scores,
            'Средний балл аттестата': attestat_avg,
            'Общий балл при поступлении': round(total_score, 2),
            'Специальность': specialty,
            'Адрес регистрации': address,
            'Номер мобильного телефона': phone
        }
        data.append(entry)

df = pd.DataFrame(data)

for subj in subjects:
    df[subj] = df['Баллы ЦТ/ЦЭ'].apply(lambda x: x[subj])

plt.figure(figsize=(12, 8))
for subj in subjects:
    avg_scores = df.groupby('Год поступления')[subj].mean()
    plt.plot(avg_scores.index, avg_scores.values, marker='o', label=subj)
plt.title('Динамика среднего балла за ЦТ/ЦЭ по предметам')
plt.xlabel('Год')
plt.ylabel('Средний балл')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
avg_attestat = df.groupby('Год поступления')['Средний балл аттестата'].mean()
plt.plot(avg_attestat.index, avg_attestat.values, marker='o', color='blue')
plt.title('Динамика среднего балла аттестата')
plt.xlabel('Год')
plt.ylabel('Средний балл аттестата')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
passing_scores = df.groupby(['Год поступления', 'Специальность'])['Общий балл при поступлении'].mean().unstack()
passing_scores.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Динамика проходного балла по специальностям')
plt.xlabel('Год')
plt.ylabel('Проходной балл')
plt.legend(title='Специальность')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
specialty_counts = df['Специальность'].value_counts()
specialty_counts.plot(kind='bar', color='green')
plt.title('Количество поступивших студентов по специальностям')
plt.xlabel('Специальность')
plt.ylabel('Количество')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 6))
form_counts = df['Форма обучения'].value_counts()
form_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Статистика по формам обучения')
plt.ylabel('')
plt.show()

print(df)
df.to_csv('data.csv', index=False)