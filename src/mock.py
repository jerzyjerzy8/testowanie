class User:
    def __init__(self, name, age, accounts):
        self.name = name
        self.age = age
        self.accounts = accounts

    def get_available_funds(self):
        available_funds = 0
        for account in self.accounts:
            available_funds += account.get_balance()
        return available_funds
