class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}
        self.accounts = {}
        self.next_client_id = 1
        self.next_account_number = 1

    def create_client(self, name, passport_number):
        client_id = self.next_client_id
        self.next_client_id += 1
        client = Bank_Client(client_id, name, passport_number, self)
        self.clients[client_id] = client
        return client

    def get_client(self, client_id):
        if client_id in self.clients:
            return self.clients[client_id]
        return None

    def create_account(self, client_id, currency):
        if client_id not in self.clients:
            raise ValueError("Клиент не существует")
        account_number = self.next_account_number
        self.next_account_number += 1
        client = self.clients[client_id]
        account = Bank_Account(account_number, client, currency)
        self.accounts[account_number] = account
        client.accounts[account_number] = account
        return account

    def close_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Счёт не существует")
        account = self.accounts[account_number]
        if account.balance != 0:
            raise ValueError("Баланс счёта должен быть нулевым для закрытия")
        client = account.client
        del client.accounts[account_number]
        del self.accounts[account_number]

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        return None


class Bank_Client:
    def __init__(self, client_id, name, passport_number, bank):
        self.client_id = client_id
        self.name = name
        self.passport_number = passport_number
        self.bank = bank
        self.accounts = {}

    def create_account(self, currency):
        return self.bank.create_account(self.client_id, currency)

    def close_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Счёт не принадлежит этому клиенту")
        account = self.accounts[account_number]
        if account.balance != 0:
            raise ValueError("Баланс счёта должен быть нулевым для закрытия")
        self.bank.close_account(account_number)

    def top_up_account(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Счёт не принадлежит этому клиенту")
        self.accounts[account_number].top_up_account(amount)

    def withdraw_money(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Счёт не принадлежит этому клиенту")
        self.accounts[account_number].withdraw_money(amount)

    def transfer_money(self, from_account_number, to_account_number, amount):
        if from_account_number not in self.accounts:
            raise ValueError("Исходный счёт не принадлежит этому клиенту")
        if to_account_number not in self.bank.accounts:
            raise ValueError("Счёт получателя не существует")
        from_account = self.accounts[from_account_number]
        to_account = self.bank.accounts[to_account_number]
        from_account.transfer_money(to_account, amount)

    def list_accounts(self):
        if not self.accounts:
            return "Нет счетов."
        lines = []
        for acc_num, acc in self.accounts.items():
            line = "Счёт " + str(acc_num) + ": " + acc.currency + " " + str(acc.balance)
            lines.append(line)
        return "\n".join(lines)

    def get_total_balance(self):
        return sum(acc.balance for acc in self.accounts.values())


class Bank_Account:
    def __init__(self, account_number, client, currency, balance=0.0):
        self.account_number = account_number
        self.client = client
        self.currency = currency
        self.balance = balance

    def top_up_account(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount

    def withdraw_money(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount

    def transfer_money(self, to_account, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if self.currency != to_account.currency:
            raise ValueError("Несоответствие валют")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        to_account.balance += amount


bank = Bank("МойБанк")
current_client = None

while True:
    if current_client is None:
        print("\n=== Меню входа в банк ===")
        print("1. Вход по ID клиента")
        print("2. Создать нового клиента")
        print("3. Выход")
        choice = input("Выберите опцию (1-3): ").strip()

        if choice == "1":
            try:
                client_id = int(input("Введите ID клиента: "))
                current_client = bank.get_client(client_id)
                if current_client:
                    print("Добро пожаловать, " + current_client.name + "! (ID: " + str(client_id) + ")")
                else:
                    print("Неверный ID клиента. Попробуйте снова.")
                    continue
            except ValueError:
                print("Неверный ввод. ID клиента должен быть числом.")
                continue

        elif choice == "2":
            name = input("Введите имя: ").strip()
            passport = input("Введите номер паспорта: ").strip()
            if not name or not passport:
                print("Имя и паспорт обязательны.")
                continue
            current_client = bank.create_client(name, passport)
            print("Новый клиент создан! Ваш ID: " + str(current_client.client_id))

        elif choice == "3":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Выберите 1-3.")
            continue

    else:
        print("\n=== Меню клиента " + current_client.name + " (ID: " + str(current_client.client_id) + ") ===")
        print("1. Создать счёт")
        print("2. Список счетов")
        print("3. Закрыть счёт")
        print("4. Пополнить счёт")
        print("5. Снять деньги")
        print("6. Перевести деньги")
        print("7. Сгенерировать выписку (сохранить в файл)")
        print("8. Выход из аккаунта")
        choice = input("Выберите опцию (1-8): ").strip()

        try:
            if choice == "1":
                currency = input("Введите валюту (например, USD): ").strip().upper()
                if not currency:
                    raise ValueError("Валюта обязательна.")
                account = current_client.create_account(currency)
                print("Счёт создан: " + str(account.account_number) + " (" + currency + ")")

            elif choice == "2":
                accounts_info = current_client.list_accounts()
                print("\nВаши счета:")
                print(accounts_info)

            elif choice == "3":
                acc_num = int(input("Введите номер счёта для закрытия: "))
                current_client.close_account(acc_num)
                print("Счёт " + str(acc_num) + " закрыт.")

            elif choice == "4":
                acc_num = int(input("Введите номер счёта: "))
                amount = float(input("Введите сумму для пополнения: "))
                current_client.top_up_account(acc_num, amount)
                print("Пополнено " + str(amount) + " на счёт " + str(acc_num) + ".")

            elif choice == "5":
                acc_num = int(input("Введите номер счёта: "))
                amount = float(input("Введите сумму для снятия: "))
                current_client.withdraw_money(acc_num, amount)
                print("Снято " + str(amount) + " со счёта " + str(acc_num) + ".")

            elif choice == "6":
                from_acc = int(input("Введите номер исходного счёта (ваш): "))
                to_acc = int(input("Введите номер счёта получателя: "))
                amount = float(input("Введите сумму для перевода: "))
                current_client.transfer_money(from_acc, to_acc, amount)
                print("Переведено " + str(amount) + " с " + str(from_acc) + " на " + str(to_acc) + ".")

            elif choice == "7":
                filename = "выписка_" + str(current_client.client_id) + ".txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("Выписка для клиента: " + current_client.name + " (ID: " + str(
                        current_client.client_id) + ")\n")
                    f.write("Паспорт: " + current_client.passport_number + "\n\n")
                    f.write("Счета:\n")
                    total = 0.0
                    for acc_num, acc in current_client.accounts.items():
                        line = "- Счёт " + str(acc_num) + ": " + acc.currency + " " + str(acc.balance) + "\n"
                        f.write(line)
                        total += acc.balance
                    f.write("\nОбщий баланс: " + str(total))
                print("Выписка сохранена в " + filename)

            elif choice == "8":
                print("Выход из аккаунта...")
                current_client = None

            else:
                print("Неверный выбор. Выберите 1-8.")
                continue
        except ValueError as e:
            print("Ошибка: " + str(e))
        except Exception as e:
            print("Неожиданная ошибка: " + str(e))
