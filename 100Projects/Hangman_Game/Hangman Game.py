import random
import Stages
import Hangman_words
chosen_word = random.choice(Hangman_words.word_list)

print(Stages.logo)

print("Welcome to Kaustubh's Hangman's Game: ")
print("You have total 6 lives! ")
print(f'Pssst, the solution is {chosen_word}.')
print(Stages.stages[6])
display = []

for letter in chosen_word:
    display.append("_")
lives = 6
display2 = ' '.join(display)
print(display2)
count = 0
while lives != 0 and '_' in display:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess} letter: ")
        print(Stages.stages[lives])
        continue

    index = 0
    while index != -1:
        index = chosen_word.find(guess, index)
        if index != -1:
            display[index] = guess
            index += 1
            previous_guess = guess
            continue
        if index == -1:
            if chosen_word.find(guess) == -1:
                print(f"{guess} is not in the chosen word. You lose a life.")
                lives -= 1
                previous_guess = guess
                break
    display2 = ' '.join(display)
    previous_guess = guess
    print(Stages.stages[lives])
    print(display2)
if lives == 0:
    print("You lost!")
else:
    print("You won!")
