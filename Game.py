import random
words = {
    "travel": ["destination", "excursion", "passenger", "tourist", "route"],
    "language": ["english", "germany", "chinese", "ukrainian", "spanish"],
    "coffee": ["espresso", "cappuchino", "latte", "filter", "americano"],
    "colors": ["green", "white", "black", "yellow", "brown"],
    "professions": ["teacher", "doctor", "manager", "economist", "barista"]
}

def greetings():
    print("Welcome to the game Gallows!",
          "Game rules: You need to enter the letter that you think is in the word from the selected category. ",
          "If you didn't guess correctly, the number of attempts decreases. When guessing, the letter will be shown in the word",
          "The game will be over if you have exhausted all attempts, or guessed the word.",
          "Important: Do not enter numbers, symbols, spaces, or multiple letters. Only one letter must be entered.",
          "The number of attempts due to incorrect input is not reduced.",
          "Good luck!", "Please, choose one of these themes:", sep="\n")
    print(*[key for key in words])


def filter_letter():
    al = []
    for i in range(97, 123):
        al.append(chr(i))
    if letter in al:
        return True
    else:
        print("Wrong input! You must use only letter!")



greetings()
enter = input("Enter the theme: ")
while enter not in [key for key in words]:
    print("Wrong input! Try again!")
    enter = input("Enter the theme: ")
if enter in [key for key in words]:
    a = random.choice(words[enter])
    word = ["_" for i in a]
    attempts = len(a)+5
    used=[]
    print(f"Your word has {len(a)} letters and you have {attempts} attempts")
    while True:
        letter = input("Enter the letter: ")
        while letter in used:
            print("You have already entered this letter!")
            letter = input("Enter the letter: ")
        used.append(letter)
        while filter_letter() != True:
            letter = input("Enter the letter: ")
        if letter in a:
            for i, c in enumerate(a):
                if c == letter:
                    word[i] = letter
            print(*word)
            if "_" not in word:
                    print("Congratulations!")
                    print(f"Your word is {a}")
                    print("You win!")
                    break
        else:
            attempts -= 1
            print(f"This letter isn't in word. You have {attempts} attempts")
        if attempts == 0:
            print(f"Unfortunately, you couldn't guess the word! Your word was {a}!", "Game over!", sep="\n")
            break

