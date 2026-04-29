class Account :
    def __init__(self, bal , acc) :
        self.Balance=bal
        self.Account_no=acc

    def debit(self, amount):
        self.Balance-=amount
        print("Rs", amount, "has been debited ")
        print("total balance= ",self.get_balance())

    def credit(self, amount):
        self.Balance += amount
        print("Rs", amount , "has been credited")
        print("total balance= ", self.get_balance())

    def get_balance(self):
        return self.Balance
    
acc1= Account(100000, 2005)
acc1.debit(5000)