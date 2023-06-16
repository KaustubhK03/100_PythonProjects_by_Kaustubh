import random
from art import logo
rand_int = random.randint(1, 100)
print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")
difficulty_level = input("Choose a difficulty level: type 'easy' or 'hard': ").lower()


def play_game(num):
    count = 0
    if difficulty_level == 'easy':
        lives = 10
    else:
        lives = 6
    if lives != 0:
        print(f"you have {lives} lives")
    while lives != 0:
        guess = int(input("Enter a guess: "))
        if guess == num:
            count += 1
            print("That is the right number!")
            print(f"It took you {count} guesses.")
            break
        else:
            if guess < rand_int:
                print("Too low")
            elif guess > rand_int:
                print("Too high")
            else:
                print()
            count += 1
            lives -= 1
            print(f"You have {lives} lives left.")
    if lives == 0:
        print("You lost! & the number I was thinking about was: ", rand_int)


play_game(num=rand_int)
