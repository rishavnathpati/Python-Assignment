class bank:
    def __init__(self, name, ac_no, type, bal):
        self.name = name
        self.ac_no = ac_no
        self.type = type
        self.balance = bal

    def deposite(self, value):
        self.balance += value

    def withdraw(self, value):
        if(value > self.balance):
            print("Insufficient Balance!!!")
        else:
            self.balance -= value

    def show(self):
        print("Name:", self.name)
        print("Balance: ", self.balance)


c1 = bank("Rishav Nath Pati", 15587463, "Basic", 50014)

c1.show()
c1.deposite(20000)
c1.show()
c1.withdraw(10000)
c1.show()
