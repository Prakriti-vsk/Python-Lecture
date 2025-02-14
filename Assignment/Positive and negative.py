def check_number(value):
    if value > 0:
        print(f"{value} is a positive number.")
    elif value < 0:
        print(f"{value} is a negative number.")
    else:
        print(f"{value} is zero.")


try:
    number = float(input("Enter a number: "))
    check_number(number)
except ValueError:
    print("Invalid input! Please enter a valid number.")
