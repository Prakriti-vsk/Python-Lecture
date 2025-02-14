def vowel_or_consonant(letter):
    letter = letter.lower()


    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    
    elif letter.isalpha():  
        print(f"{letter} is a consonant.")
    else:
        print(f"{letter} is not a valid alphabet letter.")

try:
    letter = input("Enter a letter: ")

    if len(letter) == 1:
        vowel_or_consonant(letter)
    else:
        print("Please enter a single letter.")
except ValueError:
    print("Invalid input! Please enter a valid letter.")
