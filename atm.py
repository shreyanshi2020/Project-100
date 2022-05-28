class Atm:
    def __init__(self, acoount_number):
        self.account_number = account_number
    def view_balance(self):
        print("view_balance function")
    def cash_deposit(self):
        print("cash deposit function")
    def cash_widrawl(self):
        print("cah widrawl function")
account1 = Atm("123456")
account1.view_balance()
account1.cash_deposit()
account1.cash_widrawl()

account2 = Atm("654321")
account2.view_balance()
account2.cash_deposit()
account2.cash_widrawl()
        