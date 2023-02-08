class Account: 
    def __init__(self, owner, balance): 
        self.owner = owner 
        self.balance = balance 
        pass 
 
 
    def deposit(self): 
        self.depo = int(input()) 
        self.balance += self.depo 
 
    def withdraw(self, sum): 
        self.min = sum 
        print(f'Напоминание: Вы не можете снять более чем {self.balance} тенге') 
        if self.min > self.balance: 
            print("Error, limit") 
        elif self.balance - self.min < 0: 
            print("Error") 
        else:  
            self.balance -= self.min 
            print (f'Ostatok:{self.balance}') 
         
 
Bank1 = Account('Alibaba', 100000) 
 
min = int(input()) 
Bank1.withdraw(min)
