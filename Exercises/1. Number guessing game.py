import random

def guessing_game():
    number = random.randint(0, 100)
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        user_guess = int(input("Please enter your guess: "))
        guess_count += 1
        if number == user_guess:
            print("Congratulations, you won!")
            break
        elif number > user_guess:
            print(f'Too low')
        elif number < user_guess:
            print(f'Too high')
    else:
        print("You've used all your guesses, better luck next time!")


guessing_game()
