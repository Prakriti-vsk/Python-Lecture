Name = input("Enter your name : ")
Roll_no = input("Enter your roll no: ")

def calculate_grade(marks):
    if marks>= 90:
        return 'A+'
    if marks>= 80:
        return 'A'
    if marks>= 70:
        return 'B+'
    if marks>= 60:
        return 'B'
    if marks>= 50:
        return 'C+'
    if marks>= 40:
        return 'C'
    else:
        return 'Fail'

def marksheet():
    print("Enter marks for the following Subjects")

    try:
        math = float(input("Maths : "))
        english = float(input("English : "))
        science = float(input("Science : "))
        history = float(input("History : "))
        computer = float(input("Computer : "))

        total_marks = math + english + science + history + computer
        average_marks = total_marks/3


        math_grade = calculate_grade(math)
        science_grade = calculate_grade(science)
        english_grade = calculate_grade(english)
        history_grade = calculate_grade(history)
        computer_grade = calculate_grade(computer)

        print("\nMarksheet:")
        print(f"Maths: {math}  Grade: {math_grade}")
        print(f"Science: {science}  Grade: {science_grade}")
        print(f"English: {english}  Grade: {english_grade}")
        print(f"History: {history}  Grade: {history_grade}")
        print(f"Computer: {computer}  Grade: {computer_grade}")
        print(f"\nTotal Marks: {total_marks} / 500")
        print(f"Average Marks: {average_marks}")

        if average_marks >= 90:
            overall_grade = 'A+'
        elif average_marks >= 80:
            overall_grade = 'A'
        elif average_marks >= 70:
            overall_grade = 'B+'
        elif average_marks >= 60:
            overall_grade = 'B'
        elif average_marks >= 50:
            overall_grade = 'C+'
        elif average_marks >= 40:
            overall_grade = 'C'
        else:
            overall_grade = 'F'

        print(f"Overall Grade: {overall_grade}")

    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")
marksheet()

        
    
