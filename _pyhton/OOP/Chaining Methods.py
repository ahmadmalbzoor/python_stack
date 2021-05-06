class user:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.balance=0
    
    def make_deposit(self,amount):
        self.balance +=amount
        return self
    def make_withdrow(self,amount):
        self.balance -=amount
        return self
    def transfer(self,amount,user1,user3):
       user3.make_deposit(amount)
       user1.make_withdrow(amount)
        
user1=user("ahmad","ahmad@gmail.com")
user2=user("mohammad","mohammad@gmail.com")
user3=user("khaled","khaled@gmail.com")
user1.transfer(1000,user1,user3)

user1.make_deposit(100).make_deposit(100).make_deposit(200).make_withdrow(350)
user2.make_deposit(600).make_deposit(390).make_withdrow(433).make_withdrow(339)
user3.make_deposit(900).make_withdrow(339).make_withdrow(300).make_withdrow(300)
print(user1.name,user1.email,user1.balance)
print(user2.name,user2.email,user2.balance)
print(user3.name,user3.email,user3.balance)
print(user.transfer)