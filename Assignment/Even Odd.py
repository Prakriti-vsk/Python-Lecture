def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

try:
    number = int(input("Enter a number: "))
    even_or_odd(number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
