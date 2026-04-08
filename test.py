# Написать класс сотрудники. экземпляр класса с аргументами: имя, должность, стаж.
# Методы: приходить на работу, уходить с работы, выполнять задачи, получать зп.
# Обязательно прописать какую-то свою ошибку.
# Пользовательский ввод: добавить сотрудника, выбрать его действие (ушел с работы, пришел на работу)
class Employee:
    def __init__(self, name, post, experience):
        self.name = name
        self.post = post
        self.experience = experience
        self.is_at_work = False

    def come_to_work(self):
        self.is_at_work = True
        print(f"{self.name} пришёл на работу")

    def leave_work(self):
        self.is_at_work = False
        print(f"{self.name} ушёл с работы")

    def perform_task(self):
        if not self.is_at_work:
            raise ValueError("Нельзя выполнять задачи, если не работаешь")
        print(f"{self.name} выполняет задачу")

    def get_money(self):
        if self.experience == 0:
            money = 3000
        else:
            money = 3000 + int(self.experience) * 500
        print(f"{self.name} получил {money} рублей")

employees = []

while True:
    choice = input('''Выберите действие:
    1. Добавить сотрудника 
    2. Удалить сотрудника
    3. Изменить сотрудника
    4. Вывести сотрудников 
    5. Стоп
    ''')
    if choice == '1':
        name = input("Введите имя сотрудника: ")
        post = input("Введите должность сотрудника: ")
        experience = input("Введите опыт сотрудника: ")
        employees.append(Employee(name, post, experience))
        print(f"Сотрудник {name} добавлен")

    elif choice == '2':
        name = input("Введите имя сотрудника для удаления: ")
        for emp in employees:
            if emp.name == name:
                employees.remove(emp)
                print(f"Сотрудник {emp.name} удалён")
                break
            else:
                print(f"Сотрудник {emp.name} не найден")

    elif choice == '3':
        name = input("Введите имя сотрудника для изменения: ")
        for emp in employees:
            if emp.name == name:
                while True:
                    choice2 = input('''Выберите параметр для изменения:
                    1. Изменить имя
                    2. Изменить должность
                    3. Изменить стаж
                    4. Изменить состояние (работает или нет)
                    5. Выдать задание
                    6. Выдать заработную плату
                    7. Стоп
                    ''')
                    if choice2 == '1':
                        new_name = input("Введите новое имя: ")
                        emp.name = new_name
                    if choice2 == '2':
                        new_post = input("Введите новую должность: ")
                        emp.post = new_post
                    if choice2 == '3':
                        new_experience = int(input("Введите новый опыт работы"))
                        emp.experience = new_experience
                    if choice2 == '4':
                        while True:
                            choice3 = input('''Выберите состояние:
                            1. Работает
                            2. Не работает
                            3. Стоп
                            ''')
                            if choice3 == '1':
                                if emp.is_at_work:
                                    print(f"{emp.name} уже  работает ")
                                else:
                                    emp.come_to_work()
                            elif choice3 == '2':
                                if not emp.is_at_work:
                                    print(f"{emp.name} и так не работает ")
                                else:
                                    emp.leave_work()
                            elif choice3 == '3':
                                break
                    if choice2 == '5':
                        emp.perform_task()
                    if choice2 == '6':
                        emp.get_money()
                    if choice2 == '7':
                        break
    elif choice == '4':
        if not employees:
            print("Нет сотрудников")
        else:
            for emp in employees:
                print(f"Имя: {emp.name}, Должность: {emp.post}, Стаж: {emp.experience}, На работе: {emp.is_at_work}")
    elif choice == '5':
        break
    else:
        print("Неверный выбор")