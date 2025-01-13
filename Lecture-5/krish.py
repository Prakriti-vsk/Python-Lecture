class Bank:
    def __init__(self , name , account_no , ifsc_code):
        self.name = name
        self.account_no = account_no
        self.ifsc_code = ifsc_code

    def display(self):
        print(f"hello {self.name} how are you !!")

    def detail(self):
        print(f"your account number is {self.account_no} and ifsc code is {self.ifsc_code}")

x = int(input("enter your account number :"))
y = input("Enter your ifsc code :")
c1 = Bank('krish' , x , y)
c1.display()
c1.detail()
