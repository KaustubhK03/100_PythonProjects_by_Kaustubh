import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors]
your_choice = int(input("What do you choose? type 0 for rock, 1 for paper and 2 for scissors: "))
computer_choice = random.choice(list)
if your_choice >= 3 or your_choice < 0:
  print("You have to choose either 0, 1 or 2, You lose!")
else:
    if your_choice == 0:
        print("You choose: \n")
        print(rock)
    elif your_choice == 1:
        print("You choose: \n")
        print(paper)
    else:
        print("You choose: \n")
        print(scissors)
    print("Computer Choose: \n")
    print(computer_choice)
    if your_choice == 0 and computer_choice == paper:
        print("You lost!")
    elif your_choice == 0 and computer_choice == scissors:
        print("You won!")
    elif your_choice == 1 and computer_choice == scissors:
        print("You lost!")
    elif your_choice == 1 and computer_choice == rock:
        print("You won!")
    elif your_choice == 2 and computer_choice == rock:
        print("You lost!")
    elif your_choice == 2 and computer_choice == paper:
        print("You won!")
    else:
        print("Its a tie!")
