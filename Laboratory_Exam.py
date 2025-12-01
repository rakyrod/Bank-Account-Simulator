class BankAccount: # Parent Class
    def __init__(self):
        print("Welcome to the Bank'")
        self.name = input("Enter Name: ")
        self._accountNumber = input("Enter Account Number: ")
        self.balance = 0  

    def deposit(self): #Deposit Area
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    def withdraw(self): #Withdraw Area
        amount = float(input("Enter amount to withdraw: "))

        fee = 18
        total = amount + fee

        if self.balance >= total:
            self.balance -= total
            print("You withdrew" , amount)
            print("You've charged: ", fee)
        
        else:
            print("Insufficient Balance.")

    def showBalance(self): # Display the Balance 
        print("Available Balance:", self.balance)


if __name__ == "__main__": #Printing the methods 
    s = BankAccount()
    s.deposit()
    s.withdraw()
    s.showBalance()

