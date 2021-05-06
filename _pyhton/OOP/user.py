class user:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.balance=0
        self.transfer=0
        self.search=name
    def make_deposit(self,amount):
        self.balance +=amount
    def make_withdrow(self,amount):
        self.balance -=amount
  

        
user1=user("ahmad","ahmad@gmail.com")
user2=user("mohammad","mohammad@gmail.com")
user3=user("khaled","khaled@gmail.com")
user1.make_deposit(100)
user1.make_deposit(100)
user1.make_deposit(200)
user1.make_withdrow(350)
user2.make_deposit(600)
user2.make_deposit(390)
user2.make_withdrow(433)
user2.make_withdrow(339)
user3.make_deposit(900)
user3.make_withdrow(300)
user3.make_withdrow(300)
print(user1.name,user1.email,user1.balance)
print(user2.name,user2.email,user2.balance)
print(user3.name,user3.email,user3.balance)


