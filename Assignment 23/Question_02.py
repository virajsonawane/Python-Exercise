class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self):
        amt = float(input("Enter amount to deposit: "))
        self.Amount += amt
        print("Amount deposited successfully.")

    def Withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt <= self.Amount:
            self.Amount -= amt
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    Acc1 = BankAccount("Rahul", 5000)
    Acc1.Display()
    Acc1.Deposit()
    Acc1.Withdraw()
    print("Interest:", Acc1.CalculateInterest())
    print("---------------------")

    Acc2 = BankAccount("Neha", 10000)
    Acc2.Display()
    Acc2.Deposit()
    Acc2.Withdraw()
    print("Interest:", Acc2.CalculateInterest())


if __name__ == "__main__":
    main()
