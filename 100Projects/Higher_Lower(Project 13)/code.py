import art
from replit import clear
from game_data import data
import random
game_over = False
dictionary1 = random.choice(data)
print(art.logo)
print(f"Compare A: {dictionary1['name']}, a {dictionary1['description']}, from {dictionary1['country']}")
dictionary2 = random.choice(data)
print(art.vs)
print(f"Against B: {dictionary2['name']}, a {dictionary2['description']}, from {dictionary2['country']}")
score = 0
while not game_over:
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if (dictionary1['follower_count'] > dictionary2['follower_count'] and guess == 'A') or (dictionary1['follower_count'] < dictionary2['follower_count'] and guess == 'B'):
        clear()
        score += 1
        print(art.logo)
        print(f"You got it right, Current score = {score}")
        dictionary1 = dictionary2
        print(f"Compare A: {dictionary1['name']}, a {dictionary1['description']}, from {dictionary1['country']}")
        dictionary2 = random.choice(data)
        print(art.vs)
        print(f"Against B: {dictionary2['name']}, a {dictionary2['description']}, from {dictionary2['country']}")
    else:
        clear()
        print(f"Oops! Wrong answer, Your score is {score}")
        game_over = True