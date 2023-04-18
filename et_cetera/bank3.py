class Account:
    def __init__(self):
        self._balance = 0

    def balance(self):
        return self.balance()

    def deposit(self,n):
        self._balance() += n

    def withdraw(self,n):
        self._balance() -= n

def main():
    account = Account()
    print("Balance:", account.balance())
    account.deposit(100)
    account.withdraw(50)
    print("Balance", account.balance())

if __name__ == "__main__":
    main()

