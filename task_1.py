class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}
        self.accounts = {}

    def create_client(self, name, passport_number):
        client_id = self.next_client_id
        self.next_client_id += 1
        client = Bank_Client(client_id, name, passport_number, self)
        self.clients[client_id] = client
        return client

    def create_account(self, client_id, currency):
        if client_id not in self.clients:
            print("Клиент не существует")
        account_number = self.next_account_number
        self.next_account_number += 1
        client = self.clients[client_id]
        account = Bank_Account(account_number, client, currency)
        self.accounts[account_number] = account
        client.accounts[account_number] = account
        return account

    def close_account(self, account_number):
        if account_number not in self.accounts:
            print("Счёт не существует")
        account = self.accounts[account_number]
        if account.balance != 0:
            print("Банковский счёт должен быть пустым, чтобы удалить счёт")
        client = account.client
        del client.accounts[account_number]
        del self.accounts[account_number]

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
            print("Счёт не принадлежит этому клиенту")
        account = self.accounts[account_number]
        if account.balance != 0:
            print("Банковский счёт должен быть пустым, чтобы удалить счёт")
        self.bank.close_account(account_number)
    def top_up_account(self, account_number, amount):
        if account_number not in self.accounts:
            print("Счёт не принадлежит этому клиенту")
        self.accounts[account_number].top_up_account(amount)
    def withdraw_money(self, account_number, amount):
        if account_number not in self.accounts:
            print("Счёт не принадлежит этому клиенту")
        self.accounts[account_number].withdraw_money(amount)
    def transfer_money(self, from_account_number, to_account_number, amount):
        if from_account_number not in self.accounts:
            print("Исходный счёт не принадлежит этому клиенту")
        if to_account_number not in self.bank.accounts:
            print("Конечный счёт не существует")
        from_account = self.accounts[from_account_number]
        to_account = self.bank.accounts[to_account_number]
        from_account.transfer_money(to_account, amount)

class Bank_Account:
    def __init__(self, account_number, client, currency, balance=0.0):
        self.account_number = account_number
        self.client = client
        self.currency = currency
        self.balance = balance
    def top_up_account(self, name):
    def withdraw_money(self, name):
    def transfer_money(self, name, amount):

