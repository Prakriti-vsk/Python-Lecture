from collections import Counter
import statistics

def add_strings(str1, str2):
    """Concatenate two strings."""
    return str1 + str2

def even_odd(number):
    """Check if a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

def calculator(num1, num2, operation):
    """Perform basic arithmetic operations."""
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

def marsheet_calculation(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return "No numbers provided"
    return sum(numbers) / len(numbers)

def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    """Count the number of consonants in a string."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in s if char in consonants)

def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        return "No numbers provided"
    return statistics.median(numbers)

def calculate_mode(numbers):
    """Calculate the mode of a list of numbers."""
    if not numbers:
        return "No numbers provided"
    return Counter(numbers).most_common(1)[0][0]

def main():
    while True:
        print("\nChoose an option:")
        print("Menu displayed, waiting for user input.")  # Debugging print
        print("1. Add two strings")
        print("2. Check if a number is even or odd")
        print("3. Calculator")
        print("4. Marsheet calculation (average)")
        print("5. Calculate factorial")
        print("6. Reverse a string")
        print("7. Count vowels in a string")
        print("8. Count consonants in a string")
        print("9. Calculate median of numbers")
        print("10. Calculate mode of numbers")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")
        print(f"User selected option: {choice}")  # Debugging print

        if choice == '1':
            s1 = input("Enter first string: ")
            s2 = input("Enter second string: ")
            print("Result:", add_strings(s1, s2))

        elif choice == '2':
            num = int(input("Enter a number: "))
            print("The number is:", even_odd(num))

        elif choice == '3':
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            op = input("Enter operation (add, subtract, multiply, divide): ")
            print("Result:", calculator(n1, n2, op))

        elif choice == '4':
            nums = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Average:", marsheet_calculation(nums))

        elif choice == '5':
            n = int(input("Enter a number to calculate its factorial: "))
            print("Factorial:", factorial(n))

        elif choice == '6':
            s = input("Enter a string to reverse: ")
            print("Reversed string:", reverse_string(s))

        elif choice == '7':
            s = input("Enter a string to count vowels: ")
            print("Number of vowels:", count_vowels(s))

        elif choice == '8':
            s = input("Enter a string to count consonants: ")
            print("Number of consonants:", count_consonants(s))

        elif choice == '9':
            nums = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Median:", calculate_median(nums))

        elif choice == '10':
            nums = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Mode:", calculate_mode(nums))

        elif choice == '11':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
