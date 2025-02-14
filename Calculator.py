print("*****Calculator*****")
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y!=0:
        return x / y
    else:
        return("Error in dividing by zero")
def calaculator():
    print("Select Operation: ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

choice = input("Enter no. b/w 1 to 4 to select operation : \n")
if choice in ['1','2','3','4']:
    num1=float(input("Enter your number : "))
    num2=float(input("Enter your number : "))

    if choice=='1':
               print(f"{num1} + {num2} = {add(num1,num2)}")
    elif choice=='2':
               print(f"{num1} - {num2} = {subtract(num1,num2)}")
    elif choice=='3':
               print(f"{num1} * {num2} = {multiply(num1,num2)}")
    elif choice=='4':
               print(f"{num1} / {num2} = {divide(num1,num2)}")
else:
    print("Invalid Choice")










        
           
                      
                      
                      








           
    
